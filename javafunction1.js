
var image_index=0;
     document.onkeydown = function(e) { 
     switch(e.which) { 
     case 37: 
     try{ 
     image_index=image_index-1;
    displayImage(array[image_index], array[image_index],array[image_index], array[image_index], 512, 512);
     if (image_index >= 0){ 
     displayImage(array[image_index], array[image_index],array[image_index], array[image_index], 512, 512);} else {image_index=0}
     break;
     } catch (e) { 
 } 
     case 38:
     try{ 
     image_index=image_index+1;

     if (image_index < array.length){ 
     displayImage(array[image_index], array[image_index],array[image_index], array[image_index], 512, 512);} else {image_index=array.length-1}
     break;
     } catch (e) { 
 } 
     case 39: 
     try{ 
     image_index=image_index+1;

     if (image_index < array.length){ 
     displayImage(array[image_index], array[image_index],array[image_index], array[image_index], 512, 512);} else {image_index=array.length-1}
     break;
     } catch (e) { 
 } 
     case 40: 
     try{ 
     image_index=image_index-1;

     if (image_index >= 0){ 
     displayImage(array[image_index], array[image_index],array[image_index], array[image_index], 512, 512);} else {image_index=0}
     break;
     } catch (e) { 
 } 
     default: return; 
     } 
     e.preventDefault(); 
     };


