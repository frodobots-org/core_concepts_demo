# Frodobots Core Concepts Demo
A repository designed to expose the reader to the core concepts of the Frodobots Network:
1. Proof-Of-Drive
2. Drive-To-Earn
3. Kalman Filters & Sensor Fusion


## Proof-Of-Drive
Enter the the folder and run the demo. 

```
cd distance_measurement
python distance_measurement.py
```

This demo reads sample 3df IMU data from and returns the distance travelled by a hypthothetical Frodobot. 


## Drive-To-Earn
On receiving proof that the robot has travelled a certain distance, and the necessary checks have been completed, the host account deposits FBTL tokens using the command line cli to the driver's wallet address received by the front-end. Drivers are paid in <b>FBT Litecoin (FBTL)</b>, at a rate of 1 FBTL every 50m driven. Currently, there is a supply of `1000 FBTL` held by the minting authority - to supply 50km worth of proven drives.\n

During a drive, the moving robot pings the remote server to make FBTL payments every 50ms, on successful verification of a virtually driven robot. 

```
cd drive_to_earn
python token_payments.py <mint_authority> <driver_pk>
```

## Kalman Filters & Sensor Fusion





