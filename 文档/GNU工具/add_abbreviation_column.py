#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为GNU Coreutils命令翻译对照表添加拼音简写列
"""

import re

def get_pinyin_abbreviation(chinese_text):
    """获取中文文本的拼音首字母缩写（简化版）"""
    if not chinese_text or chinese_text == "待翻译":
        return ""
    
    # 简化的拼音首字母映射表（常用汉字）
    pinyin_map = {
        '架': 'j', '构': 'g', 'b': 'b', '2': '2', '校': 'x', '验': 'y',
        '文': 'w', '件': 'j', '名': 'm', '基': 'j', '础': 'c', '编': 'b', '码': 'm',
        '查': 'c', '看': 'k', '安': 'a', '全': 'q', '上': 's', '下': 'x', '境': 'j',
        '更': 'g', '改': 'g', '组': 'z', '权': 'q', '限': 'x', '所': 's', '有': 'y',
        '者': 'z', '切': 'q', '换': 'h', '根': 'g', '目': 'm', '录': 'l',
        '比': 'b', '较': 'j', '复': 'f', '制': 'z', '分': 'f', '割': 'g',
        '剪': 'j', '切': 'q', '日': 'r', '期': 'q', '转': 'z', '换': 'h', '拷': 'k',
        '磁': 'c', '盘': 'p', '空': 'k', '间': 'j', '列': 'l', '出': 'c',
        '颜': 'y', '色': 's', '路': 'l', '径': 'j', '大': 'd', '小': 'x',
        '显': 'x', '示': 's', '环': 'h', '变': 'b', '量': 'l', '表': 'b',
        '制': 'z', '符': 'f', '达': 'd', '式': 's', '计': 'j', '算': 's',
        '因': 'y', '数': 's', '解': 'j', '假': 'j', '值': 'z', '格': 'g',
        '折': 'z', '叠': 'd', '用': 'y', '户': 'h', '头': 't', '部': 'b',
        '主': 'z', '机': 'j', 'I': 'i', 'D': 'd', '身': 's', '份': 'f',
        '安': 'a', '装': 'z', '连': 'l', '接': 'j', '终': 'z', '止': 'z',
        '进': 'j', '程': 'c', '硬': 'y', '链': 'l', '登': 'd', '陆': 'l',
        '创': 'c', '建': 'j', '夹': 'j', '发': 'f', '布': 'b', '件': 'j',
        '接': 'j', '口': 'k', '唯': 'w', '一': 'y', '修': 'x', '改': 'g',
        '优': 'y', '先': 'x', '级': 'j', '行': 'x', '号': 'h', '忽': 'h',
        '略': 'l', '挂': 'g', '断': 'd', '处': 'c', '理': 'l', '器': 'q',
        '数': 's', '字': 'z', '八': 'b', '进': 'j', '储': 'c', '粘': 'n',
        '贴': 't', '检': 'j', '查': 'c', '信': 'x', '息': 'x', '打': 'd',
        '印': 'y', '输': 's', '出': 'c', '排': 'p', '列': 'l', '索': 's',
        '引': 'y', '当': 'd', '前': 'q', '读': 'd', '取': 'q', '绝': 'j',
        '对': 'd', '删': 's', '除': 'c', '空': 'k', '运': 'y', '行': 'x',
        '序': 'x', '彻': 'c', '底': 'd', '随': 's', '机': 'j', '打': 'd',
        '乱': 'l', '休': 'x', '眠': 'm', '排': 'p', '序': 'x', '拆': 'c',
        '分': 'f', '状': 'z', '态': 't', '缓': 'h', '冲': 'c', '调': 't',
        '整': 'z', '设': 's', '置': 'z', '和': 'h', '同': 't', '步': 'b',
        '倒': 'd', '尾': 'w', '三': 's', '通': 't', '测': 'c', '试': 's',
        '超': 'c', '时': 's', '真': 'z', '截': 'j', '断': 'd', '拓': 't',
        '扑': 'p', '设': 's', '备': 'b', '系': 'x', '统': 't', '信': 'x',
        '息': 'x', '空': 'k', '格': 'g', '去': 'q', '重': 'z', '解': 'j',
        '除': 'c', '链': 'l', '接': 'j', '时': 's', '谁': 's', '在': 'z',
        '我': 'w', '是': 's', '连': 'l', '续': 'x', '详': 'x', '细': 'x',
        '化': 'h'
    }
    
    abbreviation = ''
    for char in chinese_text:
        if char in pinyin_map:
            abbreviation += pinyin_map[char]
        elif char.isalpha():
            abbreviation += char.lower()
        else:
            # 对于未映射的字符，保留原字符
            abbreviation += char
    
    return abbreviation

def process_markdown_table():
    """处理Markdown表格，添加简写列"""
    
    # 读取文件
    with open('/home/cq/Documents/中文rust/gnu-coreutils/文档/GNU工具/命令翻译对照表.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分割成行
    lines = content.split('\n')
    
    # 找到表格开始和结束的位置
    table_start = -1
    table_end = -1
    
    for i, line in enumerate(lines):
        if line.startswith('| 序号 | 命令 | 中文翻译 |'):
            table_start = i
        elif table_start != -1 and line.strip() == '' and i > table_start + 5:
            table_end = i
            break
    
    if table_start == -1:
        print("未找到表格")
        return
    
    # 处理表头
    header_line = lines[table_start]
    new_header = header_line.replace('| 文档状态 | 文档链接 |', '| 简写 | 文档状态 | 文档链接 |')
    lines[table_start] = new_header
    
    # 处理分隔线
    separator_line = lines[table_start + 1]
    new_separator = separator_line.replace('|----------|----------|', '|------|----------|----------|')
    lines[table_start + 1] = new_separator
    
    # 处理数据行
    for i in range(table_start + 2, table_end):
        line = lines[i]
        if line.startswith('|') and '`' in line:
            # 提取中文翻译部分
            parts = line.split('|')
            if len(parts) >= 4:
                chinese_translation = parts[3].strip()
                # 计算拼音简写
                abbreviation = get_pinyin_abbreviation(chinese_translation)
                
                # 重构该行，插入简写列
                new_parts = parts[:4] + [f' {abbreviation} '] + parts[4:]
                lines[i] = '|'.join(new_parts)
    
    # 写回文件
    with open('/home/cq/Documents/中文rust/gnu-coreutils/文档/GNU工具/命令翻译对照表.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print("表格已成功更新，添加了简写列")

if __name__ == '__main__':
    try:
        process_markdown_table()
    except ImportError:
        print("需要安装pypinyin库: pip install pypinyin")
    except Exception as e:
        print(f"处理过程中出现错误: {e}")
