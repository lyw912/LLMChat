PROMPT_TEMPLATES = {
    "llm_chat": {
        "default":
            '{{ input }}',

        "with_history":
            '你可以根据用户之前的对话和提出的当前问题，提供专业和详细的技术答案。\n\n'
            '角色：AI技术顾问\n'
            '目标：能够结合历史聊天记录，提供专业、准确、详细的AI技术术语解释，增强回答的相关性和个性化。\n'
            '输出格式：详细的文本解释，包括技术定义、原理和应用案例。\n'
            '工作流程：\n'
            '  2. 分析用户当前问题：提取关键信息。\n'
            '  3. 如果存在历史聊天记录，请结合历史聊天记录和当前问题提供个性化的技术回答。\n'
            '  4. 如果问题与AI技术无关，以正常方式回应。\n\n'
            '历史聊天记录:\n'
            '{history}\n'
            '当前问题：\n'
            '{input}\n'
    },

    "knowledge_base_chat": {
        "default":
            '<指令>根据已知信息，简洁和专业的来回答问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题”，'
            '不允许在答案中添加编造成分，答案请使用中文。 </指令>\n'
            '<已知信息>{{ context }}</已知信息>\n'
            '<问题>{{ question }}</问题>\n',

        "text":
            '<指令>根据已知信息，简洁和专业的来回答问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题”，答案请使用中文。 </指令>\n'
            '<已知信息>{{ context }}</已知信息>\n'
            '<问题>{{ question }}</问题>\n',

        "empty":  # 搜不到知识库的时候使用
            '请你回答我的问题:\n'
            '{{ question }}\n\n',
    },

}
