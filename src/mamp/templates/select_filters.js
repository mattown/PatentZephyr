
var map = {};

$MAP_GEN


function showSubForm() {

    var selopt = document.getElementById("opts").value;
    var selsubopt = document.getElementById("sub_opts"+selopt).value;
    var s = selopt+'_'+selsubopt;
    resetDatatype();
    console.log (s);
    console.log ('4_3' == s);
    console.log (map['4_3']);
    console.log (selsubopt);
    document.getElementById(map[s]).style.display = "block";

}


function resetMaintype() {

    document.getElementById("main_type").style.display = "none";

}


function resetSubtype() {
    //gen below
$RESET_ALL_LIST

}

function resetDatatype() {
    document.getElementById("date_data").style.display = "none";
    document.getElementById("numeric_data").style.display = "none";
    document.getElementById("text_data").style.display = "none";
}





function resetAll() {
    //document.getElementById("f1").style.display = "none";
    resetDatatype();
    resetSubtype();
}






function showForm() {
        var selopt = document.getElementById("opts").value;
        if (selopt == 0) {
            resetAll();
        }
        else
        {
            resetSubtype();
            document.getElementById("f"+selopt).style.display = "block";
        }



    }