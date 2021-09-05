# ** Pass a common field data to all instances:
a  = SampleSerializer(data = data,many=True)
a.save({'phone_no':'1234'})

