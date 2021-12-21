function checkbox_disable ( flag ) {
    for (let i = 0; i < document.checkbox.elements.length; i++) {
        document.checkbox[i].disabled = flag;        
    }
}


function action_select_list () {
    const ids = ["factor1", "factor3", "factor4", "factor5", "factor611", "factor612", "factor62", "factor63", "factor64", "factor65", "factor66", "factor67"];

    let len = document.checkbox.elements.length;
    
    let all_or_part = document.getElementsByName("all_or_part");
    if ( all_or_part[0].checked ) {
        document.getElementById("factor6").style.display = 'block';
        document.getElementById("factor61").style.display = 'block';
    
        for (let i = 0; i < len; i++) {
            document.getElementById(ids[i]).style.display = 'block';
        }
    } else if ( all_or_part[1].checked ) {
        for (let i = 0; i < len; i++) {
            if ( document.checkbox[i].checked ) {
                document.getElementById(ids[i]).style.display = 'block';
            } else {
                document.getElementById(ids[i]).style.display = 'none';
            }
        }

        // if ( !document.checkbox[5].checked && !document.checkbox[6].checked ) { // 機能要求除外
        if ( !document.checkbox[4].checked && !document.checkbox[5].checked ) {
            document.getElementById("factor61").style.display = 'none';
        } else {
            document.getElementById("factor61").style.display = 'block';
        }
    
        let flag6 = 0;
        // for (let i = 5; i < len; i++) { // 機能要求除外
        for (let i = 4; i < len; i++) {
                if ( document.checkbox[i].checked ) {
                flag6 = 1;
                break;
            }
        }
        if (flag6) {
            document.getElementById("factor6").style.display = 'block';
        } else {
            document.getElementById("factor6").style.display = 'none';
        }
    }
}
