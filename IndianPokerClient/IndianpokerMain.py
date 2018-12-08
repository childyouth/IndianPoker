
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QStackedLayout, QMainWindow)

class IndianPokerMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.StackedLayout = QStackedLayout()
        self.StackedLayout.addWidget(self.login())
        self.StackedLayout.addWidget(self.MainUI())
        self.MainWidget = QWidget()
        self.MainWidget.setLayout(self.StackedLayout)
        self.setCentralWidget(self.MainWidget)

    def Cliked(self):
        self.StackedLayout.setCurrentIndex(1 if self.StackedLayout.currentIndex() == 0 else 0)

    def MainUI(self):
        self.setGeometry(750, 300, 350, 500)

        #제목
        self.name = QLabel('IndianPoker')
        font = self.name.font()
        font.setPointSize(font.pointSize() + 30)
        self.name.setFont(font)

        nameLayout = QHBoxLayout()
        nameLayout.addStretch(1)
        nameLayout.addWidget(self.name)
        nameLayout.addStretch(1)

        #상태창 표시
        self.statusbar = QLabel('상대방을 기다리는 중입니다.')
        self.acceptBtn = QPushButton('확인')

        statusLayout = QHBoxLayout()
        statusLayout.addStretch(1)
        statusLayout.addWidget(self.statusbar)
        statusLayout.addStretch(1)
        statusLayout.addWidget(self.acceptBtn)
        statusLayout.addStretch(1)

        #총 금액 및 상대방 배팅 표시
        self.totalbetName = QLabel('총 배팅액 : ')
        self.totalbet = QLabel('0')
        self.opponentbetName = QLabel('상대방 배 팅: ')
        self.opponentbet = QLabel('0')

        betLayout = QHBoxLayout()
        betLayout.addStretch(1)
        betLayout.addWidget(self.totalbetName)
        betLayout.addWidget(self.totalbet)
        betLayout.addStretch(1)
        betLayout.addWidget(self.opponentbetName)
        betLayout.addWidget(self.opponentbet)
        betLayout.addStretch(1)

        #돈 관련 나타내기
        self.availaleMoney = QLabel("남은 돈 : 5000")
        self.betLabel = QLabel("베팅할 금액 :")
        self.betmoney = QLineEdit()

        monryLayout = QHBoxLayout()
        monryLayout.addStretch(1)
        monryLayout.addWidget(self.availaleMoney)
        monryLayout.addStretch(1)
        monryLayout.addWidget(self.betLabel)
        monryLayout.addWidget(self.betmoney)


        #배팅
        self.bet = QPushButton("베팅")
        self.call = QPushButton("콜")
        self.allin = QPushButton("올인")
        self.die = QPushButton("포기")

        BetLayout = QHBoxLayout()
        BetLayout.addWidget(self.bet)
        BetLayout.addWidget(self.call)
        BetLayout.addWidget(self.allin)
        BetLayout.addWidget(self.die)


        #카드 숫자 나타내기
        self.numofCard = QLabel("남은 카드 : 2장")

        nowsetting = QHBoxLayout()
        nowsetting.addStretch(1)
        nowsetting.addWidget(self.numofCard)
        nowsetting.addStretch(1)


        #카드
        self.opponentCard = QLabel('1')
        self.myCard = QLabel('4')
        font = self.opponentCard.font()
        font.setPointSize(font.pointSize() + 70)
        self.opponentCard.setFont(font)
        self.myCard.setFont(font)

        CardLayout = QHBoxLayout()
        CardLayout.addStretch(1)
        CardLayout.addWidget(self.opponentCard)
        CardLayout.addStretch(1)
        CardLayout.addWidget(self.myCard)
        CardLayout.addStretch(1)

        MainLayout = QVBoxLayout()
        MainLayout.addLayout(nameLayout)
        MainLayout.addLayout(statusLayout)
        MainLayout.addLayout(betLayout)
        MainLayout.addLayout(monryLayout)
        MainLayout.addLayout(BetLayout)
        MainLayout.addLayout(nowsetting)
        MainLayout.addLayout(CardLayout)

        wiget = QWidget()
        wiget.setLayout(MainLayout)
        return wiget
        #self.setLayout(MainLayout)
        #self.setWindowTitle("PlayIndianPoker")


    def login(self):

        #제목
        self.name = QLabel('IndianPoker')
        font = self.name.font()
        font.setPointSize(font.pointSize() + 30)
        self.name.setFont(font)

        nameLayout = QHBoxLayout()
        nameLayout.addStretch(1)
        nameLayout.addWidget(self.name)
        nameLayout.addStretch(1)


        #닉네임
        self.nicknameLabel = QLabel('닉네임 : ')
        self.nickname = QLineEdit()

        nickNameLayout = QHBoxLayout()
        nickNameLayout.addStretch(1)
        nickNameLayout.addWidget(self.nicknameLabel)
        nickNameLayout.addWidget(self.nickname)
        nickNameLayout.addStretch(1)

        #방 번호
        self.roomNumLabel = QLabel('방번호 : ')
        self.roomNum = QLineEdit()

        roomNumLayout = QHBoxLayout()
        roomNumLayout.addStretch(1)
        roomNumLayout.addWidget(self.roomNumLabel)
        roomNumLayout.addWidget(self.roomNum)
        roomNumLayout.addStretch(1)

        #주소
        self.urlServer = QLineEdit()

        urlServerLayout = QHBoxLayout()
        urlServerLayout.addStretch(1)
        urlServerLayout.addWidget(self.urlServer)
        urlServerLayout.addStretch(1)

        #입장
        self.Enter = QPushButton("입장하기")
        self.Enter.clicked.connect(self.Cliked)

        EnterLayout = QHBoxLayout()
        EnterLayout.addStretch(2)
        EnterLayout.addWidget(self.Enter)
        EnterLayout.addStretch(2)

        #전체 Layout
        loginLayout = QVBoxLayout()
        loginLayout.addStretch(1)
        loginLayout.addLayout(nameLayout)
        loginLayout.addStretch(1)
        loginLayout.addLayout(nickNameLayout)
        loginLayout.addLayout(roomNumLayout)
        loginLayout.addStretch(1)
        loginLayout.addLayout(EnterLayout)
        loginLayout.addStretch(1)
        loginLayout.addLayout(urlServerLayout)

        widget = QWidget()
        widget.setLayout(loginLayout)

        return widget
        #MainWindow.setLayout(loginLayout)
        #MainWindow.setWindowTitle("LoginIndianPoker")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = IndianPokerMain()
    game.show()
    sys.exit(app.exec_())