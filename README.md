# Frodobots Core Concepts Demo
A repository designed to expose the reader to the core concepts of the Frodobots Network:
1. Proof-Of-Drive
2. Drive-To-Earn


## Proof-Of-Drive
The core concept behind the Proof-Of-Drive Algorithm is that virtually driving a robot produces measurable physical motion, which can be used by an independent arbitor to verify that:
i) The Robot was moved from point A to point B
ii) The Robot was virtually driven by Virtual Driver D during this period. 

Enter the the folder and run the demo. 

I. Measurable Distance

This script provides the most basic example of calculating the distance travelled by a robot during a virtual drive. Real Accelerometer data provided in the `sample_3df_data.csv` file is used to calculate the distance travelled by the robot.

```
cd distance_measurement
python distance_measurement.py
```


II. One-to-One Driver Connection

### Kalman Filters & Sensor Fusion


## Drive-To-Earn
On receiving proof that the robot has travelled a certain distance, and the necessary checks have been completed, the host account deposits FBTL tokens using the command line cli to the driver's wallet address received by the front-end. Drivers are paid in <b>FBT Litecoin (FBTL)</b>, at a rate of 1 FBTL every 50m driven. Currently, there is a supply of `1000 FBTL` held by the minting authority - to supply 50km worth of proven drives.\n

During a drive, the moving robot pings the remote server to make FBTL payments every 50ms, on successful verification of a virtually driven robot. 

```
cd drive_to_earn
python token_payments.py <mint_authority> <driver_pk>
```







