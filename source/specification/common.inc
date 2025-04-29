@startuml
hide circles
hide methods
skinparam DefaultFontSize 14
skinparam DefaultFontName "Arial"



<style>
package {
        LineColor gray
        FontColor gray
}



class {

        BackgroundColor white-aliceblue
        header {
                FontColor #white
                BackgroundColor #8800ff
                 FontStyle bold
        }

}


.extern {
        class {
                header {
                        BackgroundColor #gray
                }
        }

}

</style>

hide <<extern>> stereotype


@enduml
