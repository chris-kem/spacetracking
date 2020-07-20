#include <stdio.h>
#include <string.h>
#include <survive_api.h>
#include <os_generic.h>
#include "MQTTClient.h"

#define ADDRESS     "localhost"
#define CLIENTID    "HTCVive"
#define TOPIC       "examples"
#define QOS         1

static volatile int keepRunning = 1;

#ifdef __linux__

#include <assert.h>
#include <signal.h>
#include <stdlib.h>

void intHandler(int dummy) {
	if (keepRunning == 0)
		exit(-1);
	keepRunning = 0;
}

#endif

static void log_fn(SurviveSimpleContext *actx, SurviveLogLevel logLevel, const char *msg) {
	fprintf(stderr, "SimpleApi: %s\n", msg);
}

int main(int argc, char **argv) {
#ifdef __linux__
	signal(SIGINT, intHandler);
	signal(SIGTERM, intHandler);
	signal(SIGKILL, intHandler);
#endif

	MQTTClient client;
 	MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
	MQTTClient_message pubmsg = MQTTClient_message_initializer;
    	MQTTClient_deliveryToken token;
    	int rc;

    	MQTTClient_create(&client, ADDRESS, CLIENTID,
        MQTTCLIENT_PERSISTENCE_NONE, NULL);
    	conn_opts.keepAliveInterval = 20;
    	conn_opts.cleansession = 1;

    	if ((rc = MQTTClient_connect(client, &conn_opts)) != MQTTCLIENT_SUCCESS)
    	{
        	printf("Failed to connect, return code %d\n", rc);
        	exit(-1);
    	}


	SurviveSimpleContext *actx = survive_simple_init_with_logger(argc, argv, log_fn);
	if (actx == 0) // implies -help or similiar
		return 0;

	survive_simple_start_thread(actx);

	for (const SurviveSimpleObject *it = survive_simple_get_first_object(actx); it != 0;
		 it = survive_simple_get_next_object(actx, it)) {
		printf("Found '%s'\n", survive_simple_object_name(it));
	}

	while (survive_simple_wait_for_update(actx) && keepRunning) {
		for (const SurviveSimpleObject *it = survive_simple_get_next_updated(actx); it != 0;
			 it = survive_simple_get_next_updated(actx)) {
			SurvivePose pose;
			uint32_t timecode = survive_simple_object_get_latest_pose(it, &pose);
			//printf("%s %s (%u): %f %f %f %f %f %f %f\n", survive_simple_object_name(it),
			//	   survive_simple_serial_number(it), timecode, pose.Pos[0], pose.Pos[1], pose.Pos[2], pose.Rot[0],
			//	   pose.Rot[1], pose.Rot[2], pose.Rot[3]);
                        //printf("%s %s (%u): %.2f %.2f %.2f\n", survive_simple_object_name(it),
                          //       survive_simple_serial_number(it), timecode, pose.Pos[0], pose.Pos[1], pose.Pos[2]);

			//char payloadString[] = {(char)pose.Pos[0] + ";" + (char)pose.Pos[1] + ";" + (char)pose.Pos[2] + ";"};
			//char payloadString[] = {(char)pose.Pos[0] +";")};
			//strncat(payloadString, (char)pose.Pos[1] +";");
			//strncat(payloadString, (char)pose.Pos[2] +";");
			char payloadString[200];
			sprintf(payloadString, "%.2f;%.2f;%.2f;%.2f\n", pose.Pos[0], pose.Pos[1], pose.Pos[2]);
			//sprintf(payloadString, "%s", ";");
                        //sprintf(payloadString, "%.2f", pose.Pos[1]);
                        //sprintf(payloadString, "%s", ";");
                        //sprintf(payloadString, "%.2f", pose.Pos[2]);
                        //sprintf(payloadString, "%s", ";");
			//char string[20];
			//strncpy(string, payloadString, 20);
			pubmsg.payload = payloadString;
    			pubmsg.payloadlen = strlen(payloadString);
    			pubmsg.qos = QOS;
    			pubmsg.retained = 0;
			printf("%s\n", payloadString);
    			MQTTClient_publishMessage(client, TOPIC, &pubmsg, &token);
    		}

		struct SurviveSimpleEvent event = {0};

		while (survive_simple_next_event(actx, &event) != SurviveSimpleEventType_None) {
			switch (event.event_type) {
			case SurviveSimpleEventType_ButtonEvent: {
				const struct SurviveSimpleButtonEvent *button_event = survive_simple_get_button_event(&event);
				printf("%s button event %d %d\n", survive_simple_object_name(button_event->object),
					   (int)button_event->event_type, button_event->button_id);
			}
			case SurviveSimpleEventType_None:
				break;
			}
		}
	}
	printf("Cleaning up\n");
        MQTTClient_disconnect(client, 10000);
        MQTTClient_destroy(&client);
        //return rc;
	survive_simple_close(actx);
	return 0;
}
