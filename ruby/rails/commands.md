# Rails

## Generators

``` sh
# Generate a controller with actions `home` and `help`
$ rails generate controller StaticPages home help
# Generate a controller without the test framework files (e.g. RSpec)
$ rails generate controller Cowboy --no-test-framework
# Delete all the files made by the StaticPages controller generation
$ rails destroy StaticPages
```

## Migrations

``` sh
# Run the migrations with
$ rake db:migrate
# Undo a single migration step
$ rake db:rollback
# Go all the way back to the beginning
$ rake db:migrate VERSION=0
```


