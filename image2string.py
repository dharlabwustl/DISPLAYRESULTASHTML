import base64
import pandas as pd

def write_html_empty_table(n_row,n_col,mode,table_filename):
    with open(table_filename, mode) as file:
        file.write('<table style="width:100%">\n')
        file.write('<tr>\n')
        for x in range(n_col):
            file.write('<th id=header'+ str(x) + '>Contact</th>\n')
        file.write('</tr>\n')
        for x in range(n_row):
            file.write('<tr>\n')
            for y in range(n_col):
                file.write('<td id=row'+ str(x) + '_col_' + str(y)+ '>Contact</th>\n')
            file.write('</tr>\n')
        file.write('</table>\n')


#     <table style="width:100%">
# <tr>
# <th id="header1" >Company</th>
# <th>Contact</th>
# <th>Country</th>
# </tr>
# <tr>
# <td>Alfreds Futterkiste</td>
# <td>Maria Anders</td>
# <td>Germany</td>
# </tr>
# <tr>
# <td>Centro comercial Moctezuma</td>
# <td>Francisco Chang</td>
# <td>Mexico</td>
# </tr>
# </table>

## write header
# print(converted_string)
def writetextfromafile_toanother(htmlfile,mode,headerfile):
    with open(headerfile, "r") as header_file:
        header_txt = header_file.read()
    with open(htmlfile, mode) as file:
        file.write(header_txt)
def write_text(htmlfile,mode,text):
    with open(htmlfile, mode) as file:
        file.write(text)
def image2base64(image_filename):
    with open(image_filename, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    return converted_string

def push_image_in_javascript_variable(converted_string,arrayname,htmlfilename):
    with open(htmlfilename, "a") as file:
        file.write('\n')
        file.write('src="data:image/png;base64, ')
    with open(htmlfilename, "ab") as file:
        file.write(converted_string)
    with open(htmlfilename, "a") as file:
        file.write('"\n')
        file.write(arrayname+'.push(src)\n')
    ############################
def push_imagefile_asbase64_in_javascript_var(image_filename,arrayname,htmlfile):
    image_filename_base64=image2base64(image_filename)
    push_image_in_javascript_variable(image_filename_base64,arrayname,htmlfile)
## write javascript function
htmlfile="encode_1.html"
headerfile="header.html"
writetextfromafile_toanother(htmlfile,"w",headerfile)
df = pd.DataFrame(data={'col1': [1, 2], 'col2': [4, 3]})
write_text(htmlfile,'a',df.to_html(classes="table table-dark",index=False).replace('<th>','<th style ="background-color: royalblue; color: white">'))
write_html_empty_table(2,4,'a',htmlfile)
javascript_file= "begin_javascript.js"
writetextfromafile_toanother(htmlfile,"a",javascript_file)
javascript_file= "javafunction.js"
writetextfromafile_toanother(htmlfile,"a",javascript_file)
image_filename="Normal-CT-head-5Age-30-40.jpg"
push_imagefile_asbase64_in_javascript_var(image_filename,'array',htmlfile)
push_imagefile_asbase64_in_javascript_var(image_filename,'array1',htmlfile)
push_imagefile_asbase64_in_javascript_var(image_filename,'array2',htmlfile)
push_imagefile_asbase64_in_javascript_var(image_filename,'array3',htmlfile)
javascript_file= "javafunction1.js"
writetextfromafile_toanother(htmlfile,"a",javascript_file)
javascript_file= "javafunction2.js"
writetextfromafile_toanother(htmlfile,"a",javascript_file)
javascript_file= "end_javascript.js"
writetextfromafile_toanother(htmlfile,"a",javascript_file)
footerfile="footer.txt"
writetextfromafile_toanother(htmlfile,"a",footerfile)
#     function_to_write = '    var img = document.createElement("img");\
#     var img1 = document.createElement("img");\
#     var img2 = document.createElement("img"); \
#     var img3 = document.createElement("img"); \
#     function displayImage(src, width, height) {\
#     img.src = src; \
#     img.width = width; \
#     img.height = height; \
#     document.body.appendChild(img); \
#     img1.src = src; \
#     img1.width = width; \
#     img1.height = height; \
#     document.body.appendChild(img1); \
#     img2.src = src; \
#     img2.width = width; \
#     img2.height = height; \
#     document.body.appendChild(img2);\
#     img3.src = src; \
#     img3.width = width; \
#     img3.height = height; \
#     document.body.appendChild(img3); \
#     }'
# ## write source images
#
# ## display images
# ## write footer
# def write_footer(htmlfile,headerfile):
#     with open(headerfile, "r") as header_file:
#         header_txt = header_file.read()
#     with open(htmlfile, "w") as file:
#         file.write(header_txt)
# with open("header.html", "r") as header_file:
#     header_txt = header_file.read()
# with open('encode.html', "w") as file:
#     file.write(header_txt)
#
# with open("ct-brain-contrast.jpg", "rb") as image2string:
#     converted_string = base64.b64encode(image2string.read())
# with open("Normal-CT-head-5Age-30-40.jpg", "rb") as image2string:
#     converted_string1 = base64.b64encode(image2string.read())
#
# with open('encode.html', "w") as file:
#     file.write(header_txt)
#     df = pd.DataFrame(data={'col1': [1, 2], 'col2': [4, 3]})
#     file.write(df.to_html(classes="table table-dark",index=False).replace('<th>','<th style ="background-color: royalblue; color: white">'))
#     file.write("\n")
#     #####################
#     file.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
#     file.write('<script>\n')
#     # file.write('</script>\n')
#     # file.write('<script>\n')
#     #############################
# #     <figure>
# # <img src="https://images.unsplash.com/photo-1477346611705-65d1883cee1e?auto=format&fit=crop&w=1000&q=80"
# # loading="lazy" alt="Mountain landscape" width="600" height="400" />
# # <figcaption>
# # Mountain landscape by
# # <a href="https://unsplash.com/@heytowner">John Towner</a>.
# # </figcaption>
# # </figure>
#
# ###############################
#
#     function_to_write = '    var img = document.createElement("img");\
#     var img1 = document.createElement("img");\
#     var img2 = document.createElement("img"); \
#     var img3 = document.createElement("img"); \
#     function displayImage(src, width, height) {\
#     img.src = src; \
#     img.width = width; \
#     img.height = height; \
#     document.body.appendChild(img); \
#     img1.src = src; \
#     img1.width = width; \
#     img1.height = height; \
#     document.body.appendChild(img1); \
#     img2.src = src; \
#     img2.width = width; \
#     img2.height = height; \
#     document.body.appendChild(img2);\
#     img3.src = src; \
#     img3.width = width; \
#     img3.height = height; \
#     document.body.appendChild(img3); \
#     }'
#     file.write('var array= new Array();')
#     file.write('var array1= new Array();')
#     file.write('var array2= new Array();')
#     file.write('var array3= new Array();')
#     file.write(function_to_write + '\n')
#
#
# with open('encode.html', "a") as file:
#     file.write('\n')
#     file.write('src="data:image/png;base64, ')
# with open('encode.html', "ab") as file:
#     file.write(converted_string)
# with open('encode.html', "a") as file:
#     file.write('"\n')
#     file.write('array.push(src)\n')
# ############################
# with open('encode.html', "a") as file:
#     file.write('\n')
#     file.write('src="data:image/png;base64, ')
# with open('encode.html', "ab") as file:
#     file.write(converted_string1)
# with open('encode.html', "a") as file:
#     file.write('"\n')
#     file.write('array.push(src)\n')
# ################################
# with open('encode.html', "a") as file:
#     file.write('\n')
#     # file.write('array.push(src)\n')
#     # file.write('array.push(src)\n')
#     # file.write('array.push(src)\n')
#     # file.write('array.push(src)\n')
#     # displayImage(array[0], 512, 512);
#     file.write('displayImage(array[0], 512, 512);\n')
#     file.write('\n')
#     function_to_write='var image_index=0; \
#     document.onkeydown = function(e) { \
#     switch(e.which) { \
#     case 37: \
#     try{ \
#     image_index=image_index-1;\
#     if (image_index >= 0){ \
#     displayImage(array[image_index], 512, 512);} else {image_index=0}\
#     break;\
#     } catch (e) { \
# } \
#     case 38:\
#     try{ \
#     image_index=image_index+1;\
#     if (image_index < array.length){ \
#     displayImage(array[image_index], 512, 512);} else {image_index=array.length-1}\
#     break;\
#     } catch (e) { \
# } \
#     case 39: \
#     try{ \
#     image_index=image_index+1;\
#     if (image_index < array.length){ \
#     displayImage(array[image_index], 512, 512);} else {image_index=array.length-1}\
#     break;\
#     } catch (e) { \
# } \
#     case 40: \
#     try{ \
#     image_index=image_index-1;\
#     if (image_index >= 0){ \
#     displayImage(array[image_index], 512, 512);} else {image_index=0}\
#     break;\
#     } catch (e) { \
# } \
#     default: return; \
#     } \
#     e.preventDefault(); \
#     };'
#     file.write(function_to_write + '\n')
#     file.write('</script>\n')
#
#
#     file.write('</body>\n')
#     file.write('</html>\n')
#
# # file.write(converted_string)
