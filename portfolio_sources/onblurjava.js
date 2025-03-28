function s_rate() {
    // Shirt calculation
    var s_qty = document.getElementById("s_qty").value;
    var s_rate = 550;
    var s_total = s_qty * s_rate;
    document.getElementById("s_total").value = s_total;
}
function t_rate() {
    // Toys calculation
    var t_qty = document.getElementById("t_qty").value;
    var t_rate = 330;
    var t_total = t_qty * t_rate;
    document.getElementById("t_total").value = t_total;
}
function tr_rate() {
    // Trouser calculation
    var tr_qty = document.getElementById("tr_qty").value;
    var tr_rate = 700;
    var tr_total = tr_qty * tr_rate;
    document.getElementById("tr_total").value = tr_total;
}
function sn_rate() {
    // Sneakers calculation
    var sn_qty = document.getElementById("sn_qty").value;
    var sn_rate = 1200;
    var sn_total = sn_qty * sn_rate;
    document.getElementById("sn_total").value = sn_total;
  }
  
  function totalbill() {
    // Calculate total bill
    var s_total = parseFloat(document.getElementById("s_total").value) || 0;
    var t_total = parseFloat(document.getElementById("t_total").value) || 0;
    var tr_total = parseFloat(document.getElementById("tr_total").value) || 0;
    var sn_total = parseFloat(document.getElementById("sn_total").value) || 0;
  
    var bill = s_total + t_total + tr_total + sn_total;
    document.getElementById("bill").value = bill;
  }
  