fun main(arg:Array<String>){
    var lista:MutableList<Int> = mutableListOf<Int>()
    for (i in 1..4){
        val valor:Int = readLine()!!.toInt()
        lista.add(valor)
    }
    val res:Int = lista[0] * lista[1] - lista[2] * lista[3]
    println("DIFERNCA = $res")
}