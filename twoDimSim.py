print "######################## 2D simulation ################"

base_distance=10000.0 # m
explorer_speed=9000.0 # m/hr
explorer_operation_time=5.0 # hr
explorer_operation_distance=explorer_speed*explorer_operation_time
recharge_time=3.5 # hr
number_of_rechargers=4.0
recharger_speed=4000.0 # m/hr

for i in range(0,number_of_rechargers):
	distance=base_distance+(i+1)*explorer_operation_distance
	time=distance/recharger_speed+(i)*recharge_time
	print "Recharger #",i+1,"should be deployed",time,"hours befor start of mission"
total_length=(number_of_rechargers+1)*explorer_operation_distance
total_time=total_length/explorer_speed+number_of_rechargers*recharge_time
print "Total exploration length was",total_length
print "Total operation time was",total_time
print "Total downtime was",number_of_rechargers*recharge_time