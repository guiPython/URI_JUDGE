import java.lang.IndexOutOfBoundsException
import java.lang.NumberFormatException
import kotlin.String as String1

fun mdc(a:Int,b:Int):Int = if (b==0) a else mdc(b, a%b)

fun pot (a:Int,b:Int):Int = if(b==0) 1 else a*pot(a,b-1)

fun Ternas (tripla:List<Int>): String1 {
    val (x,y,z) = tripla.sorted()
    if (pot(x,2) + pot(y,2) == pot(z,2)){
        if (mdc(mdc(x,y),z) == 1){
            return "tripla pitagorica primitiva"
        }
        else return "tripla pitagorica"
    }
    else return "tripla"
}
fun  main(arg:Array<String1>){
    while (true) {
        try {
            val(n1,n2,n3) = readLine()!!.split(' ').map (String1::toInt)
            val tripla = listOf<Int>(n1,n2,n3)
            println(Ternas(tripla))
        }
        catch (e :NumberFormatException){
            break
        }
        catch (e :IndexOutOfBoundsException){
            break
        }
    }
}

