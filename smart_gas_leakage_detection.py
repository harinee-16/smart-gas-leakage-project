"""

# Gas threshold values

import random
import time

SAFE_LEVEL = 200
WARNING_LEVEL = 500

def ai_risk_analysis(gas_value):
    if gas_value < SAFE_LEVEL:
        return "SAFE"
    elif gas_value < WARNING_LEVEL:
        return "WARNING"
    else:
        return "DANGER"

def cloud_monitoring(gas_value, status):
    print(f"[CLOUD] Gas Level: {gas_value} ppm | Status: {status}")

def emergency_alert():
    print("[ALERT] Gas Leakage Detected!")
    print("[SMS] Notification sent to user.")

def auto_ventilation():
    print("[FAN] Ventilation System Activated.")

def automatic_gas_booking():
    print("[BOOKING] New Gas Cylinder Booking Request Sent.")

def mobile_tracking():
    print("[MOBILE APP] Real-time Gas Status Updated.")

while True:
    gas_value = random.randint(100, 800)

    print("\n--------------------------------")
    print("Current Gas Level:", gas_value, "ppm")

    status = ai_risk_analysis(gas_value)

    cloud_monitoring(gas_value, status)

    if status == "SAFE":
        print("System Status: SAFE")

    elif status == "WARNING":
        print("System Status: WARNING")
        mobile_tracking()

    elif status == "DANGER":
        print("System Status: DANGER")
        emergency_alert()
        auto_ventilation()
        automatic_gas_booking()
        mobile_tracking()

    time.sleep(5)"""

"""safe_level=100

class gas_detect():
    print("gass app")

    def ai_detect(self,gas_detect):
        if gas_level>=safe_level:
            print("warning ", gas_level)
        elif gas_level>=25 and gas_level<=99:
            print("normal",gas_level)
        else:
            print("its low gas ",gas_level)

gas_level=int(input())

obj=gas_detect()
obj.ai_detect(gas_detect)"""


"""SAFE_LEVEL = 200
WARNING_LEVEL = 500

def ai_risk_analysis(gas_value):
    if gas_value < SAFE_LEVEL:
        return "SAFE"
    elif gas_value < WARNING_LEVEL:
        return "WARNING"
    else:
        return "DANGER"

def cloud_monitoring(gas_value, status):
    print(f"[CLOUD] Gas Level: {gas_value} ppm | Status: {status}")

def emergency_alert():
    print("[ALERT] Gas Leakage Detected!")
    print("[SMS] Notification sent to user.")

def auto_ventilation():
    print("[FAN] Ventilation System Activated.")

def automatic_gas_booking():
    print("[BOOKING] New Gas Cylinder Booking Request Sent.")

def mobile_tracking():
    print("[MOBILE APP] Real-time Gas Status Updated.")


def main():
    while true:
        print("1.ai_risk_analysis")
        print("2.cloud_monitoring")
        print("3.emergency_alert")
        print("4.automatic_gas_booking")
        print("5.mobile_tracking")


ch= int(input())
if ch==1:
    ch.ai_risk_analysis()
elif ch==2:
    ch.cloud_monitoring()
elif ch==3:
    ch.emergency_alert()
elif ch==4:
    ch.automatic_gas_booking()
elif ch==5:
    ch.mobile_tracking()
else:
    print("wrong")"""


SAFE_LEVEL = 200
WARNING_LEVEL = 500

def ai_risk_analysis(gas_value):
    if gas_value < SAFE_LEVEL:
        return "SAFE"
    elif gas_value < WARNING_LEVEL:
        return "WARNING"
    else:
        return "DANGER"

def cloud_monitoring(gas_value, status):
    print(f"[CLOUD] Gas Level: {gas_value} ppm | Status: {status}")

def emergency_alert():
    print("[ALERT] Gas Leakage Detected!")
    print("[SMS] Notification sent to user.")

def auto_ventilation():
    print("[FAN] Ventilation System Activated.")

def automatic_gas_booking():
    print("[BOOKING] New Gas Cylinder Booking Request Sent.")

def mobile_tracking():
    print("[MOBILE APP] Real-time Gas Status Updated.")

def main():
    while True:
        print("\n--- Gas Monitoring System ---") #
        print("1. AI Risk Analysis")
        print("2. Cloud Monitoring")
        print("3. Emergency Alert")
        print("4. Automatic Gas Booking")
        print("5. Mobile Tracking")
        print("6. Exit")

        ch = int(input("Enter your choice: "))
        

        if ch == 1:
            gas_value = int(input("Enter gas value (ppm): "))
            status = ai_risk_analysis(gas_value)
            print(f"Status: {status}")
        elif ch == 2:
            gas_value = int(input("Enter gas value (ppm): "))
            status = ai_risk_analysis(gas_value)
            cloud_monitoring(gas_value, status)
        elif ch == 3:
            emergency_alert()
        elif ch == 4:
            automatic_gas_booking()
        elif ch == 5:
            mobile_tracking()
        elif ch == 6:
            print("Exiting program...")
            break
        else:
            print("Wrong choice, try again.")

# Run the program
main()

              
              



    









