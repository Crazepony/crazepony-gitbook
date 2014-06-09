---
layout: wiki
title: 系统流程框架
---

# {{ page.title }}

介绍系统的初始化流程，以及系统任务之间的关系。

## 系统任务

最关心的是系统中由多少个任务在运行。在FreeRTOS下，任务的初始化使用函数。所以，用grep命令参看一下源代码，可以看到一共有下面这些系统初始化的任务：

```
$ grep -inIw 'xTaskCreate' -r ./hal/ ./modules/
./hal/src/eskylink.c:312:  xTaskCreate(eskylinkTask, (const signed char * const)"EskyLink",
./hal/src/pm.c:111:  xTaskCreate(pmTask, (const signed char * const)"PWRMGNT",
./hal/src/uart.c:145:  xTaskCreate(uartRxTask, (const signed char * const)"UART-Rx",
./hal/src/radiolink.c:237:  xTaskCreate(radiolinkTask, (const signed char * const)"RadioLink",
./modules/src/stabilizer.c:157:  xTaskCreate(stabilizerTask, (const signed char * const)"STABILIZER",
./modules/src/crtp.c:77:  xTaskCreate(crtpTxTask, (const signed char * const)"CRTP-Tx",
./modules/src/crtp.c:79:  xTaskCreate(crtpRxTask, (const signed char * const)"CRTP-Rx",
./modules/src/info.c:68:  xTaskCreate(infoTask, (const signed char * const)"Info",
./modules/src/log.c:171:  xTaskCreate(logTask, (const signed char * const)"log",
./modules/src/pidctrl.c:43:  xTaskCreate(pidCrtlTask, (const signed char * const)"PIDCrtl",
./modules/src/param.c:92:   xTaskCreate(paramTask, (const signed char * const)"PARAM",
./modules/src/system.c:68:  xTaskCreate(systemTask, (const signed char * const)"SYSTEM",

```

所有的任务在创建之后，都会进入`while(1)`的循环中，也就是任务一直循环运行。

## 任务之间的关系

那么任务之间的关系是怎么样的呢，如何各司其职完成系统的控制呢。下面使用一个简图进行了说明，逻辑主线是控制数据的传递。

![crazyflie task](/assets/img/crazyflie-task.png)

