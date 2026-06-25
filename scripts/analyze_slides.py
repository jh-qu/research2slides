#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('decks/hermes-agent/slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

blocks = []
current = []
in_code = False
for line in content.split('\n'):
    if line.strip().startswith('```'):
        in_code = not in_code
    if not in_code and line.strip() == '---':
        blocks.append('\n'.join(current))
        current = []
    else:
        current.append(line)
if current:
    blocks.append('\n'.join(current))

def idx(s):
    for i, b in enumerate(blocks):
        if s in b:
            return i
    return -1

titles = [
    ('cover',       'Hermes Agent'),
    ('p2_myth',     '從神話到 AI'),
    ('p3_overview', '專案概覽'),
    ('p4_models',   '多模型支援，一套框架'),
    ('p5_platform', '多平台整合'),
    ('p6_features', '六大核心技術特色'),
    ('p7_loop',     'Agent 越用越聰明'),
    ('p8_skill',    'Skill 生命週期'),
    ('p9_negative', '負面學習'),
    ('p10_soul',    'SOUL.md：Agent 行為'),
    ('p11_memory',  '記憶不中斷'),
    ('p12_search',  'session_search'),
    ('p13_prompt',  'Promptware 防禦'),
    ('p14_kanban',  'Multi-agent Kanban'),
    ('p15_gateway', 'Tool Gateway'),
    ('p16_plugin',  'Plugin 系統'),
    ('p17_reliab',  '企業可靠性'),
    ('p18_approval','指令審批機制'),
    ('p19_security','資安全貌'),
    ('p20_token',   'Token 消耗'),
    ('p21_use',     '適用場景 vs 不適用場景'),
    ('p22_break',   '實際落地案例'),
    ('p23_bot',     '遊戲營運 Bot'),
    ('p24_data',    '資料準備'),
    ('p25_social',  '社群驗證'),
    ('p26_collab',  '八種協作模式'),
    ('p27_conc',    '評估結論'),
    ('p28_ref',     '資料來源'),
    ('p29_thanks',  '謝謝'),
    ('app_title',   '# Appendix'),
    ('app_bq',      'DailyUserInfoSnapshot'),
    ('app_query',   '歷史 Query 範例'),
    ('app_ops',     '一般營運知識'),
    ('app_arch',    '架構解析'),
    ('app_curator', 'Curator 四道剎車'),
    ('app_curator2','Curator 四道剎車（續）'),
    ('app_os',      '以 OS 為邊界'),
]

for name, t in titles:
    i = idx(t)
    preview = blocks[i][:60].replace('\n', '|') if i >= 0 else 'NOT FOUND'
    print(f"  {i:3d}  {name:15s}  {t[:30]}")

print(f"\nTotal blocks: {len(blocks)}")
