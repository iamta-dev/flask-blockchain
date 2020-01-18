import hashlib
import json
from datetime import datetime as date
from flask import Flask , render_template , request , redirect

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
        block = Block( 0, "2020-01-18 15:30:23", "Genesis block", "0")
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
        # (self, index, timestamp, data, previous_hash):
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
                return index
            if currb.previous_hash != prevb.hash:
                return index
        return "isChainValid"
        
# -V1 print data show terminal
# if __name__=="__main__":
    # blockchain = BlockChain()
    # blockchain.create_dataList("4565","เล่ม 55 หน้า 56","วังทองหลวง กรุงเทพมหานคร","เนื้อที่ประมาน 3 ไร่ 1 งาน 56 ตารางวา","นายสมชาย ทวีผล","279 หมู่ 10 ต.ลำเลียง อ.กระบุรี จ.ระนอง","นางเกษร ไก่เเก้ว")
    # blockchain.generate_next_block("2020-01-18 18:30:23")
    # blockchain.create_dataList("9265","เล่ม 3 หน้า 34","คลองเตย กรุงเทพมหานคร","เนื้อที่ประมาน 100 ไร่ 5 งาน 100 ตารางวา","นายณัฐวัตร นารินทร์","279 หมู่ 10 ต.ริ่มตลิ่ง อ.คลองเตย จ.กรุงเทพมหานคร","นายนคร ลำสีหานาม")
    # blockchain.generate_next_block("2020-01-18 19:30:23")
    # blockchain.create_dataList("8957","เล่ม 124 หน้า 76","สาทร กรุงเทพมหานคร","เนื้อที่ประมาน 2000 ไร่ 9 งาน 50 ตารางวา","นางลำจวน ศิลอาชา","279 หมู่ 10 ต.สุรนารี อ.เมือง จ.นาครราขสีมา","นายสมชาย มีตัง")
    # blockchain.generate_next_block("2020-01-18 19:30:23")
#     blockchain.blocks[2].data[0]['TitleDeed']['number'] = "7773"
#     print(blockchain.isChainValid())
    # blockchain.create_dataList("ema","ta",1000)
    # blockchain.generate_next_block()
    # blockchain.create_dataList("ta","ema",81)
    # blockchain.generate_next_block() 
    # for block in blockchain.blocks:
    #     print("\n #############################################################")
    #     print("\nid   :{}".format(block.index ))
    #     print("\nhash :{}".format(block.hash ))
    #     print("\ntime :{}".format(block.timestamp ))
    #     print("\ndata :{}".format(block.data[0]))
    #     print("\npv_h :{}".format(block.previous_hash ))

    
    # blockchain.blocks[1].data[0]['amount'] = 20000000
    # for block in blockchain.blocks:
    #     print("\n #############################################################")
    #     print("\nid   :{}".format(block.index ))
    #     print("\nhash :{}".format(block.hash ))
    #     print("\ntime :{}".format(block.timestamp ))
    #     print("\ndata :{}".format(block.data ))
    #     print("\npv_h :{}".format(block.previous_hash ))


# -V2 run blockchain in web
blockchain=BlockChain()
blockchain.create_dataList("4565"," 55 หน้า 56","วังทองหลวง กรุงเทพมหานคร"," 3 ไร่ 1 งาน 56 ตารางวา","นายสมชาย ทวีผล","279 หมู่ 10 ต.ลำเลียง อ.กระบุรี จ.ระนอง","นางเกษร ไก่เเก้ว")
blockchain.generate_next_block("2020-01-18 18:30:23")
blockchain.create_dataList("9265"," 3 หน้า 34","คลองเตย กรุงเทพมหานคร"," 100 ไร่ 5 งาน 100 ตารางวา","นายณัฐวัตร นารินทร์","279 หมู่ 10 ต.ริ่มตลิ่ง อ.คลองเตย จ.กรุงเทพมหานคร","นายนคร ลำสีหานาม")
blockchain.generate_next_block("2020-01-18 19:30:23")
blockchain.create_dataList("8957"," 124 หน้า 76","สาทร กรุงเทพมหานคร"," 2000 ไร่ 9 งาน 50 ตารางวา","นางลำจวน ศิลอาชา","279 หมู่ 10 ต.สุรนารี อ.เมือง จ.นาครราขสีมา","นายสมชาย มีตัง")
blockchain.generate_next_block("2020-01-18 19:30:23")
blockchain.blocks[2].timestamp = "99999999999"

app=Flask(__name__)

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



        
