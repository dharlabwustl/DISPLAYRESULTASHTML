
var image_index=initial_slice_with_lesion;
     document.onkeydown = function(e) { 
     switch(e.which) { 
     case 37: 
     try{ 
     image_index=image_index-1;
    displayImage(array_0[image_index], array_1[image_index],array_2[image_index], array_3[image_index], 512, 512);
     if (image_index >= 0){
     displayImage(array_0[image_index], array_1[image_index],array_2[image_index], array_3[image_index], 512, 512);} else {image_index=0}
     break;
     } catch (e) {
 }
     case 38:
     try{
     image_index=image_index+1;

     if (image_index < array_0.length){
     displayImage(array_0[image_index], array_1[image_index],array_2[image_index], array_3[image_index], 512, 512);} else {image_index=array_0.length-1}
     break;
     } catch (e) {
 }
     case 39:
     try{
     image_index=image_index+1;

     if (image_index < array_0.length){
     displayImage(array_0[image_index], array_1[image_index],array_2[image_index], array_3[image_index], 512, 512);} else {image_index=array_0.length-1}
     break;
     } catch (e) {
 }
     case 40:
     try{
     image_index=image_index-1;

     if (image_index >= 0){
     displayImage(array_0[image_index], array_1[image_index],array_2[image_index], array_3[image_index], 512, 512);} else {image_index=0}
     break;
     } catch (e) { 
 } 
     default: return; 
     } 
     e.preventDefault(); 
     };



