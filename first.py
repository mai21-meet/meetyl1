list1=[2,4,6,8]
list2=[6,8,10]
def mai(red,blue):
	adam=[]
	for num in red:
		if num in blue:
			adam.append(num)
	return adam
amir=mai(list1,list2)
print(amir)
print (sum (amir))

encoder_caesar = {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l',"j":"m","k":'n','l':'o',"m":'p','n':'q',"o":'r',"p":'s','q':'t','r':'u','s':'v','t':''