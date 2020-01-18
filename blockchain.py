import hashlib
from datetime import datetime as date
from flask import Flask , render_template , request , redirect

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index 
        self.timestamp = timestamp 
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()
    def generate_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8')
        )
        return sha.hexdigest()

class BlockChain():
    def __init__(self):
        self.blocks = []
        self.dataList = []
        self.prev_block = None
        self.generate_genesis_block()
    
    def create_dataList(self,from_address,to_address,amount):
        self.dataList.append({
                'from_address': from_address,
                'to_address': to_address,
                'amount': amount,
        })

    def generate_genesis_block(self):
        block = Block( 0, date.now(), "Genesis block", "0")
        self.blocks.append(block)
        self.prev_block = block
    
    def generate_next_block(self):
        this_index = self.prev_block.index + 1
        this_date = date.now()
        previous_hash = self.prev_block.hash
        block = Block(this_index,this_date,self.dataList,previous_hash) 
        self.dataList = []
        self.blocks.append(block)
        self.prev_block = block


# -V1 print data show terminal
# if __name__=="__main__":
#     blockchain = BlockChain()
#     blockchain.create_dataList("ta","bam",0.9)
#     blockchain.generate_next_block()
#     blockchain.create_dataList("leo","ta",100)
#     blockchain.generate_next_block()
#     blockchain.create_dataList("ema","ta",1000)
#     blockchain.generate_next_block()
#     blockchain.create_dataList("ta","ema",81)
#     blockchain.generate_next_block() 
#     for block in blockchain.blocks:
#         print("\n #############################################################")
#         print("\nid   :{}".format(block.index ))
#         print("\nhash :{}".format(block.hash ))
#         print("\ntime :{}".format(block.timestamp ))
#         print("\ndata :{}".format(block.data ))
#         print("\npv_h :{}".format(block.previous_hash ))


# -V2 run blockchain in web
blockchain = BlockChain()
blockchain.create_dataList("ta","bam",0.9)
blockchain.generate_next_block()
blockchain.create_dataList("leo","ta",100)
blockchain.generate_next_block()
blockchain.create_dataList("ema","ta",1000)
blockchain.generate_next_block()
blockchain.create_dataList("ta","ema",81)
blockchain.generate_next_block()

app=Flask(__name__)

@app.route('/newBlock/',methods=['POST'])
def new_Block():
    blockchain.create_dataList(request.form['from_address'],request.form['to_address'],request.form['amount'])
    blockchain.generate_next_block()
    return redirect("http://127.0.0.1:8080/blocks")

@app.route("/blocks")
def viewBlocks():
    return render_template('blocks.html',blocks=blockchain.blocks)

@app.route("/")
def viewIndex():
    return render_template('index.html',blocks=blockchain.blocks)


if __name__=="__main__":
    app.run(debug=True, port=8080)



        
