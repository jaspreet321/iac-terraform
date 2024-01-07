from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time

def change_volume(increase=True, step=0.02):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = current_volume + step if increase else current_volume - step

    # Ensure the new volume is within the valid range [0.0, 1.0]
    new_volume = max(0.0, min(1.0, new_volume))

    # Set the new volume
    volume.SetMasterVolumeLevelScalar(new_volume, None)

if __name__ == "__main__":
    try:
        while True:
            print("Press '+' to increase volume")
            print("Press '-' to decrease volume")
            print("Press 'q' to quit")

            choice = input("Enter your choice: ").strip().lower()

            if choice == "+":
                change_volume(increase=True)
            elif choice == "-":
                change_volume(increase=False)
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please use '+' to increase, '-' to decrease, or 'q' to quit.")
            
            time.sleep(1)  # Add a delay to prevent rapid volume changes

    except KeyboardInterrupt:
        pass

