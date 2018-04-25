
import cookie

app = cookie.Cookie(__name__)

@app.cookie 
def main (string=None):
	print(string)

main()

