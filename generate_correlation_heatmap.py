import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 收集所有任务的数据
def load_all_results():
    """从三个领域的结果文件中提取所有性能指标"""
    
    data = {
        'Causal': [],
        '3D': [],
        'Boolean': []
    }
    
    # 因果图数据
    causal_dir = Path('/Users/byzantium/github/_HypoSpace/causal/results')
    for json_file in sorted(causal_dir.glob('*.json')):
        try:
            with open(json_file, 'r') as f:
                result = json.load(f)
                if 'statistics' in result:
                    stats = result['statistics']
                    data['Causal'].append({
                        'Validity': stats.get('valid_rate', {}).get('mean', 0),
                        'Uniqueness': stats.get('novelty_rate', {}).get('mean', 0),
                        'Recovery': stats.get('recovery_rate', {}).get('mean', 0),
                    })
        except:
            pass
    
    # 3D数据
    threed_dir = Path('/Users/byzantium/github/_HypoSpace/3d/results')
    for json_file in sorted(threed_dir.glob('*.json')):
        try:
            with open(json_file, 'r') as f:
                result = json.load(f)
                if 'statistics' in result:
                    stats = result['statistics']
                    data['3D'].append({
                        'Validity': stats.get('valid_rate', {}).get('mean', 0),
                        'Uniqueness': stats.get('novelty_rate', {}).get('mean', 0),
                        'Recovery': stats.get('recovery_rate', {}).get('mean', 0),
                    })
        except:
            pass
    
    # 布尔数据
    boolean_dir = Path('/Users/byzantium/github/_HypoSpace/boolean/results')
    for json_file in sorted(boolean_dir.glob('*.json')):
        try:
            with open(json_file, 'r') as f:
                result = json.load(f)
                if 'statistics' in result:
                    stats = result['statistics']
                    data['Boolean'].append({
                        'Validity': stats.get('valid_rate', {}).get('mean', 0),
                        'Uniqueness': stats.get('novelty_rate', {}).get('mean', 0),
                        'Recovery': stats.get('recovery_rate', {}).get('mean', 0),
                    })
        except:
            pass
    
    return data

def create_correlation_heatmap():
    """生成相关性热力图"""
    
    data = load_all_results()
    
    # 合并所有数据
    all_validity = []
    all_uniqueness = []
    all_recovery = []
    
    for task in ['Causal', '3D', 'Boolean']:
        for sample in data[task]:
            all_validity.append(sample['Validity'])
            all_uniqueness.append(sample['Uniqueness'])
            all_recovery.append(sample['Recovery'])
    
    # 计算相关性矩阵
    metrics_array = np.array([
        all_validity,
        all_uniqueness,
        all_recovery
    ])
    
    correlation_matrix = np.corrcoef(metrics_array)
    
    # 创建热力图 (不使用seaborn)
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 使用imshow绘制热力图
    im = ax.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1, aspect='auto')
    
    # 设置标签
    labels = ['Validity', 'Uniqueness', 'Recovery']
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    
    # 旋转标签
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # 添加数值标签
    for i in range(len(labels)):
        for j in range(len(labels)):
            text = ax.text(j, i, f'{correlation_matrix[i, j]:.3f}',
                          ha="center", va="center", color="black", fontsize=11, fontweight='bold')
    
    ax.set_title('Correlation Matrix of Performance Metrics\nAcross All Tasks', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # 添加colorbar
    cbar = plt.colorbar(im, ax=ax, label='Correlation Coefficient')
    
    plt.tight_layout()
    
    # 保存图表
    plt.savefig('/Users/byzantium/github/_HypoSpace/figs/correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.savefig('/Users/byzantium/github/_HypoSpace/figs/correlation_heatmap.svg', format='svg', bbox_inches='tight')
    
    print("✓ Correlation heatmap generated successfully!")
    print(f"\nCorrelation Matrix:")
    print(correlation_matrix)
    print(f"\nFiles saved:")
    print("  - /Users/byzantium/github/_HypoSpace/figs/correlation_heatmap.png")
    print("  - /Users/byzantium/github/_HypoSpace/figs/correlation_heatmap.svg")

if __name__ == '__main__':
    create_correlation_heatmap()
