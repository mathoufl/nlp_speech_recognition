import h5py

filename1 = "../../cmumosi/CMU_MOSI_COVAREP.csd"
filename2 = "../../cmumosi/CMU_MOSI_OpenSmile_EB10.csd"
filename3 = "../../cmumosi/CMU_MOSI_openSMILE_IS09.csd"
filename4 = "../../cmumosi/CMU_MOSI_Opinion_Labels.csd"
filename5 = "../../cmumosi/CMU_MOSI_TimestampedWordVectors.csd"
filename6 = "../../cmumosi/CMU_MOSI_Visual_Facet_41.csd"
filename7 = "../../cmumosi/CMU_MOSI_Visual_Facet_42.csd"
filename8 = "../../cmumosi/CMU_MOSI_Visual_OpenFace_1.csd"
filename9 = "../../cmumosi/CMU_MOSI_Visual_OpenFace_2.csd"

file_array = []

f1 = h5py.File(filename1, 'r')
file_array.append(f1)

f2 = h5py.File(filename2, 'r')
file_array.append(f2)

f3 = h5py.File(filename3, 'r')
file_array.append(f3)

f4 = h5py.File(filename4, 'r')
file_array.append(f4)

f5 = h5py.File(filename5, 'r')
file_array.append(f5)

f6 = h5py.File(filename6, 'r')
file_array.append(f6)

f7 = h5py.File(filename7, 'r')
file_array.append(f7)

f8 = h5py.File(filename8, 'r')
file_array.append(f8)

f9 = h5py.File(filename9, 'r')
file_array.append(f9)

def format_data(bytes_object):
    string_representation = bytes_object.decode('utf-8')
    python_list = eval(string_representation)
    return str(python_list)

with open('../dataset_summary.txt', 'a') as file :
    for f in file_array :
        temp = []
        f.visit(temp.append)
        filename = temp[0]
        file.write(filename + " : " + format_data(f[filename+'/metadata/dimension names'][()][0]) + "\n\n")
