from flask import Flask,request,jsonify

app = Flask(__name__)

class Test:
    def __init__(self,s):
        self.s = s
    def ispalindrom(self):
        self.s = ''.join(char.lower() for char in self.s if char.isalnum())
        return self.s == self.s[::-1]

@app.route("/", methods = ["GET","POST"])
def home():
 
    if request.method == "POST":
        try:
            st = request.get_json().get("st","none")
            if st == "none":
                return jsonify({"error": "Missing 'st' field"}), 400
            
            num = Test(st)
            result = num.ispalindrom()  # Directly assign boolean (not a set)
            
            return jsonify({
                "st": st,
                "result": result
            })
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    return jsonify({"message": "Send a POST request with 'st' field to check palindrome"})

if __name__ == "__main__":
    app.run(debug=True)
