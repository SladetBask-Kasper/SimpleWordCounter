# pip install pynput pyinstaller
# pyinstaller -F {the name of your python file}
# pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz

from pynput.keyboard import Key, Listener

keys = {}
def on_press(key):
	newKey = str(key)#.lower() 
	try:
		keys[newKey] += 1
	except KeyError:
		keys[newKey] = 1

try:
	if __name__ == "__main__":
		print("Press Ctrl+C in terminal to stop program and see result.")
		with Listener(on_press=on_press) as listener:
			listener.join()
except KeyboardInterrupt:
	print("Done!")
	for key in keys:
		print(f" {key}: {keys[key]}")
	exit()