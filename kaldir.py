from rembg import remove

input_path = "kedi.jpg"
output_path = "cat.jpg"

with open(input_path,'rb') as i: ##dosyayı rb-read binary olarak açar
    with open(output_path,'wb') as o: ## dosyayı yazar binary olarak
        in_file = i.read()
        output_file = remove(in_file)
        o.write(output_file)
#what is
