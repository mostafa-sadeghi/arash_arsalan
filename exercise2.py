
Hazineye_paziraee = 200
Voroudi = 100
keraye_darbast = 1000
def calculate_vehicle_number(number_of_students, vehicle_cap):
    vehicle_count = 0
    vehicle_count = number_of_students // vehicle_cap
    if number_of_students % vehicle_cap != 0:
        vehicle_count += 1
    return vehicle_count



def cost_per_student(num_of_veh, num_of_students):
    veh_cost_per_stu = (num_of_veh * keraye_darbast) / num_of_students
    all_costs_per_student = veh_cost_per_stu + Hazineye_paziraee + Voroudi
    return all_costs_per_student

number_of_stu = int(input("How many students? "))
veh_cap = int(input("enter vehicle cap: "))

num_of_veh = calculate_vehicle_number(number_of_stu, veh_cap)

print("each student must pay:",cost_per_student(num_of_veh, number_of_stu))