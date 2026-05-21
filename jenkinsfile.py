pipeline{
    agent any
    enviroment {
        PYTHON = C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python314\\python.exe

    }

    stges {
        stages("checkout code") {
            steps {
                checkout scm
            }
        }
    stages("show python version") {
        steps {
            bat "${env.PYTHON} --version"
            }
        }
    stages("run ectractfile.py") {
        steps {
            but $"{env.PYTHON} ectractfile.py"
            }
        }
    }
}
