time, distance = [int(i.split(" ")[1]) for i in open("input2.txt", "r").read().split("\n")]
holds = int((time + (time**2-4*distance)**0.5)/2) - int((time - (time**2-4*distance)**0.5)/2)
print(holds)

print(int((44806572 + (44806572**2-4*208158110501102)**0.5)/2) - int((44806572 - (44806572**2-4*208158110501102)**0.5)/2))