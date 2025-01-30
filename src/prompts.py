def get_word_definition_prompt(word_or_sentence):
    return f"""Human: You are a great dictionary that provides in-depth explanations for words and phrases. 
    For the input: '{word_or_sentence}', provide the explanation in this exact format:

    **Word Meaning:**  
    ```markdown
    > [The word]  
    > /UK pronunciation/  
    > Display English Definition (10-20 words).  
    > Chinese Translation (single line)
    ```

    **Pronunciation Reference:**  
    [Cambridge Dictionary - [The word]](https://dictionary.cambridge.org/dictionary/english/[The word])  

    **Explanation:**  
    ```markdown
    ### English Explanation
    - Detailed explanation of the word's meaning
    - Different contexts and usages
    - Common phrases or idioms

    ### 中文解释
    - 详细的中文解释
    - 使用场景和例子
    ```

    **Another Sentence Example:**  
    ```markdown
    - An example sentence with the word in bold. *(similar words in parentheses)*  
    - The same sentence translated to Chinese with the word in bold.
    ```
    Make sure to:
    1. Use the exact markdown formatting shown above
    2. Include both English and Chinese explanations
    3. Provide a practical example sentence with alternatives
    4. Use the word in context if a sentence is provided as input

    Assistant:""" 