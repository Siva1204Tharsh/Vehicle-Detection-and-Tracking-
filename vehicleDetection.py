import cv2
import imutils


cascade_src='cars.xml'

car_cascade = cv2.CascadeClassifier(cascade_src)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=1000)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, 'Car', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    
    cv2.imshow('Frame', frame)
    b=str(len(cars))
    a=int(b)
    n=a
    print("____________________________________________________________")
    print("North :%d"%(a))
    if n>=8:
        print("North More Traffic, Please on the RED Light")
    else:
        print("North Less Traffic, Please on the GREEN Light")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()