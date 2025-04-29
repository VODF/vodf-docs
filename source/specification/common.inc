@startuml
hide circles
hide methods
skinparam DefaultFontSize 14
skinparam DefaultFontName "Arial"



<style>
package {
        LineColor #gray
        FontColor #gray
}

class {

        backgroundColor white-aliceblue
        header {
                fontColor #ffffff
                backgroundColor #8800ff
                fontStyle bold
        }

}


.extern {
        class {
                header {
                        backgroundColor #gray
                }
        }

}

</style>

skinparam classStereotypeFontColor white

hide <<extern>> stereotype


@enduml
