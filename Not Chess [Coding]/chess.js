function decodeIt(match) {
  var match_length = match.length / 4;
  var main_string = "";
  for (gr = 0; gr < match_length; gr++) {
    var left = gr * 4;
    var right = left + 4;
    var gr_string = match.substring(left, right);
    var string = "   ";

    loop1:
    for (ch1 = 0; ch1 <= 255; ch1++) {
      ch1_c = String.fromCharCode(ch1);

      loop2:
      for (ch2 = 0; ch2 <= 255; ch2++) {
        ch2_c = String.fromCharCode(ch2);
        
        loop3:
        for (ch3 = 0; ch3 <= 255; ch3++) {
          string = ch1_c + ch2_c + String.fromCharCode(ch3);

          if (encodeIt(string) == gr_string) {
            alert(string)
            break loop1;
          }
        }
      }
    }
    main_string += string;
  }

  return main_string;
}

console.log(decodeIt("cXVlZW4lMjdzJTIwZ2FtYml0"));