import hashlib
import json
from datetime import datetime as date
from flask import Flask , render_template , request , redirect ,jsonify

class Block:
    def __init__(self, index, timestamp, data, previous_hash,hash=''):
        self.index = index 
        self.timestamp = timestamp 
        self.data = data
        self.previous_hash = previous_hash
        if hash == '':
            self.hash = self.generate_hash()
        else:
            self.hash=hash
        
    def generate_hash(self):
        sha = hashlib.sha512(
            str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(json.dumps(self.data, sort_keys=True)).encode('utf-8') +
            str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class BlockChain():
    def __init__(self):
        self.blocks = []
        self.dataList = []
        self.prev_block = None
        self.generate_genesis_block()
    
    def create_dataList(self, number, book, DeedAddress, area, name, OwnerAddress, verify):
        self.dataList.append({
                'TitleDeed':{
                    'number': number,
                    'book': book,
                    'address': DeedAddress,
                    'area': area
                },
                'Owner':{
                    'name': name,
                    'address': OwnerAddress
                },
                'verify':verify
        })

    def generate_genesis_block(self):
        block = Block( 0, "2020-01-18 15:30:23.345334", "Genesis block", "0")
        self.blocks.append(block)
        self.prev_block = block
    
    def generate_next_block(self,date):
        this_index = self.prev_block.index + 1
        this_date = date
        previous_hash = self.prev_block.hash
        block = Block(this_index,this_date,self.dataList,previous_hash) 
        self.dataList = []
        self.blocks.append(block)
        self.prev_block = block

    def isChainValid(self):
        self.editId = []
        for index in range(1,len(self.blocks)):
            currb=Block(self.blocks[index].index ,
                        self.blocks[index].timestamp ,
                        self.blocks[index].data ,
                        self.blocks[index].previous_hash ,
                        self.blocks[index].hash)
            prevb=Block(self.blocks[index-1].index ,
                        self.blocks[index-1].timestamp ,
                        self.blocks[index-1].data ,
                        self.blocks[index-1].previous_hash ,
                        self.blocks[index-1].hash)
            if currb.hash != currb.generate_hash():
                self.editId.append(index)
            if currb.previous_hash != prevb.hash:
                self.editId.append(index)
        
        if len(self.editId) == 0:
            return "isChainValid"
        else:
            return self.editId
        
# # -V2 run blockchain in web
blockchain=BlockChain()
blockchain.create_dataList("4565","55 หน้า 56","วังทองหลวง กรุงเทพมหานคร","3 ไร่ 1 งาน 56 ตารางวา","นายสมชาย ทวีผล","52 อาคารธนิยะพลาซา ชั้น 14 โซนบี พนนสีลม แขวงสุริยวงศ์ เขตบางรัก กรุงเทพมหานคร แขวงสุริยวงศ์ เขตบางรัก กรุงเทพมหานคร","นางเกษร ไก่เเก้ว")
blockchain.generate_next_block("2020-01-18 18:30:23.324322")
blockchain.create_dataList("9265","3 หน้า 34","คลองเตย กรุงเทพมหานคร","100 ไร่ 5 งาน 100 ตารางวา","นายณัฐวัตร นารินทร์","เลขที่ 942/170-171 ชาญอิสสระทาวเวอร์ 1 ชั้น 25 ถนนพระราม 4 แขวงสุริยวงศ์ เขตบางรัก กรุงเทพมหานคร","นายนคร ลำสีหานาม")
blockchain.generate_next_block("2020-01-18 19:30:23.904563")
blockchain.create_dataList("8957","124 หน้า 76","สาทร กรุงเทพมหานคร","2000 ไร่ 9 งาน 50 ตารางวา","นางลำจวน ศิลอาชา","เลขที่ 540 ถนนเพลินจิต แขวงลุมพินี เขตปทุมวัน กรุงเทพมหานคร 10330 แขวงลุมพินี เขตปทุมวัน กรุงเทพมหานคร","นายสมชาย มีตัง")
blockchain.generate_next_block("2020-01-18 19:30:23.245344")

blockchain.create_dataList("2352","23 หน้า 44","อำเภอแก้งสนามนาง นครราชสีมา","3 ไร่ 1 งาน 56 ตารางวา","นายปกรณ์วุฒิ อุดมพิพัฒน์สกุล","59 หมู่ 15 ถ.มิตรภาพ-หนองคาย ต.จอหอ อ.เมือง จ.นครราชสีมา","นางลินดา เชิดชัย")
blockchain.generate_next_block("2020-01-18 18:30:23.095653")
blockchain.create_dataList("0992","3 หน้า 23","อำเภอด่านขุนทด นครราชสีมา","780 ไร่ 5 งาน 100 ตารางวา","นายองค์การ ชัยบุตร","129 หมู่ 12 ถ.มิตรภาพ ต.สุรนารี อ.เมือง จ.นครราชสีมา","นายนคร ลำสีหานาม")
blockchain.generate_next_block("2020-01-18 19:30:23.123533")
blockchain.create_dataList("6723","124 หน้า 89","อำเภอโนนไทย นครราชสีมา","4000 ไร่ 9 งาน 50 ตารางวา","นางธีรัจชัย พันธุมาศ","60/9 หมู่ 15 ถ.มิตรภาพ ต.สุรนารี อ.เมือง จ.นครราชสีมา","นายสมชาย มีตัง")
blockchain.generate_next_block("2020-01-18 11:30:23.569445")

blockchain.create_dataList("2341","24 หน้า 34","อำเภอขุนตาล เชียงราย","3 ไร่ 1 งาน 56 ตารางวา","นายสุรสิทธิ์ วงศ์วิทยานันท์","425,425/1 หมู่ 22 ตำบล รอบเวียง อำเภอ เมืองเชียงราย เชียงราย","นางมงคลกิตติ์ สุขสินธารานนท์")
blockchain.generate_next_block("2020-01-18 12:30:23.123455")
blockchain.create_dataList("4522","56 หน้า 98","อำเภอเชียงของ เชียงราย","100 ไร่ 5 งาน 100 ตารางวา","นายนภาพร เพ็ชร์จินดา","33/2 หมู่ 8 ตำบล บุญเรือง อำเภอป่าแดด เชียงราย","นายยรรยงก์ ถนอมพิชัยธำรง")
blockchain.generate_next_block("2020-01-18 15:30:23.095566")
blockchain.create_dataList("9878","123 หน้า 12","อำเภอแม่ฟ้าหลวง เชียงราย","23000 ไร่ 45 งาน 67 ตารางวา","นางอารี ไกรนรา","127 หมู่ 12 ตำบล ศรีดอนชัย อำเภอ พาน เชียงราย","นายสมชาย มีตัง")
blockchain.generate_next_block("2020-01-18 22:30:23.143234")
blockchain.create_dataList("1289","23 หน้า 90","อำเภอแม่สาย เชียงราย","12000 ไร่ 33 งาน 70 ตารางวา","นางนพดล มาตรศรี","4/561 หมู่ 3 ตำบล สถาน  อำเภอ เวียงแก่น เชียงราย","นายนพดล แก้วสุพัฒน์")
blockchain.generate_next_block("2020-01-18 22:30:23.345675")

app=Flask(__name__)

@app.route('/editBlock/',methods=['POST'])
def edit_Block():
    blockchain.blocks[int(request.form['editIndex'])].data[0]['TitleDeed']['number'] = request.form['editNumber']
    blockchain.blocks[int(request.form['editIndex'])].data[0]['TitleDeed']['book'] = request.form['editBook']
    blockchain.blocks[int(request.form['editIndex'])].data[0]['TitleDeed']['address'] = request.form['editDeedAddress']
    blockchain.blocks[int(request.form['editIndex'])].data[0]['TitleDeed']['area'] = request.form['editArea']
    blockchain.blocks[int(request.form['editIndex'])].data[0]['Owner']['name'] = request.form['editName']
    blockchain.blocks[int(request.form['editIndex'])].data[0]['Owner']['address'] = request.form['editOwnerAddress']
    blockchain.blocks[int(request.form['editIndex'])].data[0]['verify'] = request.form['editVerify']
    return redirect("http://localhost:8080/")

@app.route('/newBlock/',methods=['POST'])
def new_Block():
    blockchain.create_dataList(
                request.form['number'],
                request.form['book'],
                request.form['DeedAddress'],
                request.form['area'],
                request.form['name'],
                request.form['OwnerAddress'],
                request.form['verify'])
    blockchain.generate_next_block(date.now())
    return redirect("http://localhost:8080/")

@app.route("/blocks")
def viewBlocks():
    return render_template('blocks.html',blocks=blockchain.blocks,isChainValid=blockchain.isChainValid())

@app.route("/")
def viewIndex():
    return render_template('index.html',blocks=blockchain.blocks,isChainValid=blockchain.isChainValid())


if __name__=="__main__":
    app.run(debug=True, port=8080)



# -V1 print data show terminal
# if __name__=="__main__":
#     blockchain=BlockChain()
#     blockchain.create_dataList("4565","55 หน้า 56","วังทองหลวง กรุงเทพมหานคร","3 ไร่ 1 งาน 56 ตารางวา","นายสมชาย ทวีผล","52 อาคารธนิยะพลาซา ชั้น 14 โซนบี พนนสีลม แขวงสุริยวงศ์ เขตบางรัก กรุงเทพมหานคร แขวงสุริยวงศ์ เขตบางรัก กรุงเทพมหานคร","นางเกษร ไก่เเก้ว")
#     blockchain.generate_next_block("2020-01-18 18:30:23.324322")
#     blockchain.create_dataList("9265","3 หน้า 34","คลองเตย กรุงเทพมหานคร","100 ไร่ 5 งาน 100 ตารางวา","นายณัฐวัตร นารินทร์","เลขที่ 942/170-171 ชาญอิสสระทาวเวอร์ 1 ชั้น 25 ถนนพระราม 4 แขวงสุริยวงศ์ เขตบางรัก กรุงเทพมหานคร","นายนคร ลำสีหานาม")
#     blockchain.generate_next_block("2020-01-18 19:30:23.904563")
#     blockchain.create_dataList("8957","124 หน้า 76","สาทร กรุงเทพมหานคร","2000 ไร่ 9 งาน 50 ตารางวา","นางลำจวน ศิลอาชา","เลขที่ 540 ถนนเพลินจิต แขวงลุมพินี เขตปทุมวัน กรุงเทพมหานคร 10330 แขวงลุมพินี เขตปทุมวัน กรุงเทพมหานคร","นายสมชาย มีตัง")
#     blockchain.generate_next_block("2020-01-18 19:30:23.245344")
    # blockchain.blocks[3].timestamp = "99999999999"
    # blockchain.blocks[1].data[0]['TitleDeed']['number'] = "7773"
    # print(blockchain.isChainValid())
    # for block in blockchain.blocks:
    #     print("\n #############################################################")
    #     print("\nid   :{}".format(block.index ))
    #     print("\nhash :{}".format(block.hash ))
    #     print("\ntime :{}".format(block.timestamp ))
    #     print("\ndata :{}".format(block.data[0]))
    #     print("\npv_h :{}".format(block.previous_hash ))



        
