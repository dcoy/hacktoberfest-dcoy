module helloworld where

fromString = fromColist . toCostring

main : IO Unit
main = putStrLn (fromString "Hello, World!")