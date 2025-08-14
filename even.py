from flask import Flask, request, render_template

app = Flask(__name__)

class Numbers:
    def __init__(self, n):
        self.n = n

    def even(self):
        return self.n % 2 == 0

    def odd(self):
        return self.n % 2 != 0

    def is_prime(self):
        if self.n <= 1:
            return False
        for i in range(2, int(self.n ** 0.5) + 1):
            if self.n % i == 0:
                return False
        return True

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    number = None
    check_type = None
    
    if request.method == "POST":
        try:
            number = int(request.form["number"])
            check_type = request.form["check_type"]
            
            num = Numbers(number)
            result = {
                "even": num.even(),
                "odd": num.odd(),
                "prime": num.is_prime()
            }.get(check_type)
            
        except ValueError:
            result = "Please enter a valid integer"
    
    return render_template("new.html", 
                         number=number,
                         check_type=check_type,
                         result=result)

if __name__ == "__main__":
    app.run(debug=True)