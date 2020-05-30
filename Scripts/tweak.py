with open('/root/Task3/modeltrain.py', 'r') as f:
    data = f.read()
    index = data.find("addDense(5)")
    index = index + 11

data = data[:index] +"\n" +  "addDense(10)" + data[index:]
data = data.replace('Epoch=','Epoch=20 + ')
print(data)
   
with open("/root/Task3/modeltrain.py" , "w") as f:
    f.write(data)


print("Done")
