class Star:

    type = 'Star'
    x = 100

    def change():   # 클래스 함수
        x = 200     # 위에 x와 다른 변수다 위는 클래스 변수 이것은 로컬 변수
        print('x is', x)

print('x IS ', Star.x) # OK
Star.change() # OK
print('x IS ', Star.x)

star = Star() # OK
print('x IS ', star.x) # OK     # 클래스 변수는 객체에서 호출 가능
star.change() # Error       # 클래스 함수는 객체에서 호출 불가능(클래스 함수가 인자를 받지 않아서)
# star.change() => Star.change(star) 이기 때문에 self를 사용하는 것