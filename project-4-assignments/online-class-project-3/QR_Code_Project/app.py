import qrcode
import cv2

def generate_qr(data, filename="my_qr.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"✅ QR Code saved as {filename}")

def decode_qr(filename):
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image)
    if data:
        print(f"📦 Decoded Data: {data}")
    else:
        print("❌ QR Code not detected or unreadable.")

def menu():
    while True:
        print("\n--- QR Code Encoder / Decoder ---")
        print("1. Generate QR Code")
        print("2. Decode QR Code")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            data = input("Enter data to encode: ")
            filename = input("Enter filename to save (with .png): ")
            generate_qr(data, filename)
        elif choice == '2':
            filename = input("Enter QR code image filename: ")
            decode_qr(filename)
        elif choice == '3':
            print("👋 Exiting... Thank you!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Run the menu
menu()
