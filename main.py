import random
from flask import Flask

app = Flask(__name__)
   
facts_list=["Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
            "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
            "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."]

@app.route("/")
def Selam_world():
    return '<h1>Merhaba bu sayfa bilinmeyen gerçekler hakkında bilgi verir.<a href="/Rastgele_Gercekler!!">Rastgele bir gerçeği görüntüle!</a></h1>'

@app.route("/Rastgele_Gercekler!!")
def Rastgele_Gercekler():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)
