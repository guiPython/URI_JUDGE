fun main( args:Array<String>){
    var valor:Int = readLine()!!.toInt()
    val notas = mutableListOf<Int>(100,50,20,10,5,2,1)
    for ( x in notas){
        val n_notas:Int = valor / x
        valor %= x
        println("${n_notas} nota(s) de R$ ${x} ")
    }
}