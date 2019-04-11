kg=float(input("당신의 몸무게는 몇 kg인가요?"))
heigh=float(input("당신의 키는 몇m인가요?"))

bmi=kg/heigh**2

if bmi<18.50: print("당신은 저체중입니다")
if (bmi>18.50)and(bmi<24.99): print("당신은 정상입니다")
if (bmi>24.99)and(bmi<29.99): print("당신은 과체중입니다")
if (bmi>30.00)and(bmi<34.99): print("당신은 비만입니다")
if (bmi>35.00): print("당신은 고도비만입니다")