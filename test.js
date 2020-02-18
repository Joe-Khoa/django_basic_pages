function format_no_to_str(No){
      if(No == 0){
        return '000'
      }else if(Math.floor(No/100)){ 	//abc 'a is ',a # 0
        return String(No)
      }
      else if( Math.floor(No/10)){	//abc a = 0 && b # 0
        return String('0'+No);
      }
      else {
        return String("00"+No);
      }
}

function thousand(Number){
    arr = []
    arr[5] = Math.floor(Number/Math.pow(10,5*3))
    for (i = 4; i > 0; i--){
        mod = Math.pow(10,3*(i+1))
        div = Math.pow(10,3*i)
        arr[i] = Math.floor((Number%mod)/div)
        console.log("arr["+i+"]= "+arr[i])
    }
    arr[0] = Number%1000
    console.log("arr["+0+"]= "+arr[0])
    console.log("arr["+5+"]= "+arr[5])
    return arr
}

function formatNumber(a){
    arr = thousand(a)
    Max = 0
    for (i = 5;i>-1;i--){
        if (arr[i] != 0){
            Max = i
            break
        }
    }
    console.log('Max = '+Max)
    currency_str = ''
    for(i=Max-1;i>-1;i--){
      arr[i] = format_no_to_str(arr[i])
      currency_str =  currency_str+'.'+arr[i]
    }
    arr[Max] = Number(format_no_to_str(arr[Max]))
    currency_str = arr[Max]+currency_str
    return currency_str
}
/* formatNumber(100100100987654321) */
console.log(formatNumber(50000920003330))
