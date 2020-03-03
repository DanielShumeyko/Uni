import math

file_location = "C:\\Users\\Daniel\\Desktop\\INPUT.txt"
out_location = "C:\\Users\\Daniel\\Desktop"
out_name = "OUTPUT.txt"

main_sphere = []
other_spheres = []

def intersect(s1, s2):
    if math.sqrt( (s1[0] - s2[0])**2 + (s1[1] - s2[1])**2 + (s1[2] - s2[2])**2 ) > s1[3] + s2[3]:
        return False
    return True

def any_lonely(s_list):
    if len(s_list) < 2:
        return False
    for i, sphere1 in enumerate(s_list):
        if i == len(s_list)-1:
            return False
        lonely = True
        remaining = s_list[i+1:]
        for sphere2 in remaining:
            if intersect(sphere1, sphere2):
                lonely = False
        if lonely:
            return True



with open(file_location, 'r') as f:
    lines = f.readlines()
    main_sphere = [float(i) for i in lines[0].split()]
    lines = lines[2:]
    for line in lines:
        other_spheres.append([float(i) for i in line.split()])
          

N = 0
found = False
all_spheres = []
all_spheres.append(main_sphere)

for i, sphere in enumerate(other_spheres):
    all_spheres.append(sphere)
    print(all_spheres)
    if not any_lonely(all_spheres):
        print('got here')
        N = i+1

print(N)
