# Lexical Analyzer

# Answer a:
### Rules
- Code begins with `BEGIN` and ends with `FINISH`. Each lexeme is in the code is seperated by a space.

### Statements 
- Assignment
- Declaration
- Condition
- Loops
- Boolean

## Token List

## Mathematical Operations
| Token Code | Operation | Regex |                                
|------------|-----------|-------|
| PLUS       | +         | +     |
| MINUS      | -         | -     |
| MULTIPLY   | \*        | \*    |
| DIVIDE     | /         | /     |
| MODULUS    | %         | %     |
| OPEN       | (         | )     |
| CLOSE      | )         | )     |


## Literals
| Token Code | Operation | Regex |                                
|------------|-----------|-------|
| PLUS       | +         | +     |
| MINUS      | -         | -     |
| MULTIPLY   | \*        | \*    |
| DIVIDE     | /         | /     |
| MODULUS    | %         | %     |
| OPEN       | (         | )     |
| CLOSE      | )         | )     |


## Comparisions
| Token Code | Regex     |
|------------|-----------|
| int_lit    | int_lit   |
| float_lit  | float_lit |
| bool_lit   | bool_lit  |


## Integer Types
| Token Code | Size    |
| ---------- | ------- |
| Small      | 1 byte  |
| Medium     | 2 bytes |
| Large      | 4 bytes |
| Huge       | 8 bytes |


## Keywords
| Token Code | Regex          |
|------------|----------------|
| VARIABLE   | [_a-zA-Z]{6,8} |
| ifin       | ifin           |
| LOOP       | loop           |
| STOP       | stop           |
| PLAY       | play           |
| orelse     | orelse         | 

## Other
| Token Code  | Operation | Regex |
|-------------|-----------|-------|
| ASSIGNMENT  | =         | =     |
| BLOCKBEGIN  | {         | {     |
| BLOCKFINISH | }         | }     |


# Answer b:

## Priority Order
- ()
- /
- \+
- \-
- \*
- %

## Production Rules

```txt
<stmt> --> <if_stmt> | <while_stmt> | <as_s> | <block>
<block> --> `{` { <stmt>`;` } `}`
<if_stmt> -->  `ifin` `(`<bool_expr>`)` `{` <stmt> `}` [ `orelse` `{` <stmt> `}`]
<while_loop> -->  `loop``(`<bool_expr>`)` `{` <stmt> `}`
<as_s>  --> `id` `=` <expr>
<expr> --> <term> { (`+`|`-`) <term> }
<term> --> <factor> { (`*`|`\`|`%`) <factor> }
<factor> --> `id` | `int_lit` | `float_lit` | `(` <expr> `)`
<var> -->  [_a-zA-Z]{6,8}
<datatype> --> (XS|S|L|XL)

<bool_expr> --> <band> { `OR` <band> }
<band> --> <beq> { `AND` <beq> }
<beq> --> <brel> { (`!=`|`==`) <brel> }
<brel> --> <expr> { (`<=`|`>=` | `<` | `>`) <expr> }
<expr> --> <term> { (`+`|`-`) <term> }
<term> --> <not> { (`*`|`/`|`%`) <bnot> }
<bnot> -> [!]<factor>
<factor> --> `id` | `int_lit` | `float_lit` | `bool_lit` | `(` <expr> `)`


E -> E + T          Expression + Term
E -> E - T          Expression - Term
E -> T              Some expression can be a term
T -> T * F          Term * Factor
T -> T / F          Term / Factor
T -> F              Some Terms can be Factors
F -> -F             Unary Minus
F -> +F             Unary Plus
F ->( E )           Factor can be an Expression in parentheses
F -> c              Factor can be a constant
```

### To run
run the file named fileInput.py to get the output.


## (C) Is it LL Grammar ?
The A grammar is said to be an LL grammer if it is a pairwise disjoint and has no left hand recursion. Also it is an Ll
grammar if its parsing table has atmost one production in each entry table which it does. Therefore this is an LL grammar. 

## (D) Is the Grammar Ambiguous ?
Ambiguous grammars are usually not LL. Since this grammar is LL it is not an Ambiguous grammar.