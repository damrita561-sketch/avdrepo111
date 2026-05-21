pipeline{
    agent any

    stges {
        stages("checkout code") {
            steps {
                checkout scm
            }
        }
    stages("show python version") {
        steps {
            bat python --version
            }
        }
    stages("run ectractfile.py") {
        steps {
            but python ectractfile.py
            }
        }
    }
}
