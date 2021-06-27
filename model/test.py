# -*- coding:utf-8 -*-

"""
@author: Wnstar
@time: 2017/12/14
"""
from __future__ import unicode_literals
import re

text="""
.class public Lcom/dianping/model/H5FavorConfig;
.super Lcom/dianping/model/BasicModel;
.source "H5FavorConfig.java"


# static fields
.field public static volatile synthetic $change:Lcom/dianping/android/hotfix/IncrementalChange;

.field public static final CREATOR:Landroid/os/Parcelable$Creator;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Landroid/os/Parcelable$Creator",
            "<",
            "Lcom/dianping/model/H5FavorConfig;",
            ">;"
        }
    .end annotation
.end field

.field public static final c:Lcom/dianping/archive/c;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Lcom/dianping/archive/c",
            "<",
            "Lcom/dianping/model/H5FavorConfig;",
            ">;"
        }
    .end annotation
.end field


# instance fields
.field public a:[Ljava/lang/String;
    .annotation runtime Lcom/google/gson/annotations/SerializedName;
        value = "blackList"
    .end annotation
.end field

.field public b:[Ljava/lang/String;
    .annotation runtime Lcom/google/gson/annotations/SerializedName;
        value = "whiteList"
    .end annotation
.end field


# direct methods
.method public static constructor <clinit>()V
    .locals 1

    .prologue
    .line 30
    new-instance v0, Lcom/dianping/model/H5FavorConfig$1;

    invoke-direct {v0}, Lcom/dianping/model/H5FavorConfig$1;-><init>()V

    sput-object v0, Lcom/dianping/model/H5FavorConfig;->c:Lcom/dianping/archive/c;

    .line 79
    new-instance v0, Lcom/dianping/model/H5FavorConfig$2;

    invoke-direct {v0}, Lcom/dianping/model/H5FavorConfig$2;-><init>()V

    sput-object v0, Lcom/dianping/model/H5FavorConfig;->CREATOR:Landroid/os/Parcelable$Creator;

    return-void
.end method

.method public constructor <init>()V
    .locals 2

    .prologue
    const/4 v1, 0x0

    .line 127
    invoke-direct {p0}, Lcom/dianping/model/BasicModel;-><init>()V

    .line 129
    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/dianping/model/H5FavorConfig;->isPresent:Z

    .line 130
    new-array v0, v1, [Ljava/lang/String;

    iput-object v0, p0, Lcom/dianping/model/H5FavorConfig;->b:[Ljava/lang/String;

    .line 131
    new-array v0, v1, [Ljava/lang/String;

    iput-object v0, p0, Lcom/dianping/model/H5FavorConfig;->a:[Ljava/lang/String;

    .line 132
    return-void
.end method

.method public constructor <init>(Z)V
    .locals 2

    .prologue
    const/4 v1, 0x0

    .line 134
    invoke-direct {p0}, Lcom/dianping/model/BasicModel;-><init>()V

    .line 136
    iput-boolean p1, p0, Lcom/dianping/model/H5FavorConfig;->isPresent:Z

    .line 137
    new-array v0, v1, [Ljava/lang/String;

    iput-object v0, p0, Lcom/dianping/model/H5FavorConfig;->b:[Ljava/lang/String;

    .line 138
    new-array v0, v1, [Ljava/lang/String;

    iput-object v0, p0, Lcom/dianping/model/H5FavorConfig;->a:[Ljava/lang/String;

    .line 139
    return-void
.end method


# virtual methods
.method public decode(Lcom/dianping/archive/d;)V
    .locals 4
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Lcom/dianping/archive/a;
        }
    .end annotation

    .prologue
    .line 0
    sget-object v0, Lcom/dianping/model/H5FavorConfig;->$change:Lcom/dianping/android/hotfix/IncrementalChange;

    if-eqz v0, :cond_1

    const-string v1, "decode.(Lcom/dianping/archive/d;)V"

    const/4 v2, 0x2

    new-array v2, v2, [Ljava/lang/Object;

    const/4 v3, 0x0

    aput-object p0, v2, v3

    const/4 v3, 0x1

    aput-object p1, v2, v3

    invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    .line 66
    :cond_0
    return-void

    .line 53
    :sswitch_0
    invoke-virtual {p1}, Lcom/dianping/archive/d;->b()Z

    move-result v0

    iput-boolean v0, p0, Lcom/dianping/model/H5FavorConfig;->isPresent:Z

    .line 50
    :cond_1
    :goto_0
    invoke-virtual {p1}, Lcom/dianping/archive/d;->j()I

    move-result v0

    if-lez v0, :cond_0

    .line 51
    sparse-switch v0, :sswitch_data_0

    .line 62
    invoke-virtual {p1}, Lcom/dianping/archive/d;->i()V

    goto :goto_0

    .line 56
    :sswitch_1
    invoke-virtual {p1}, Lcom/dianping/archive/d;->n()[Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/dianping/model/H5FavorConfig;->b:[Ljava/lang/String;

    goto :goto_0

    .line 59
    :sswitch_2
    invoke-virtual {p1}, Lcom/dianping/archive/d;->n()[Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/dianping/model/H5FavorConfig;->a:[Ljava/lang/String;

    goto :goto_0

    .line 51
    :sswitch_data_0
    .sparse-switch
        0xa49 -> :sswitch_0
        0x293a -> :sswitch_1
        0xd258 -> :sswitch_2
    .end sparse-switch
.end method

.method public writeToParcel(Landroid/os/Parcel;I)V
    .locals 5

    .prologue
    const/4 v0, 0x1

    const/4 v1, 0x0

    .line 0
    sget-object v2, Lcom/dianping/model/H5FavorConfig;->$change:Lcom/dianping/android/hotfix/IncrementalChange;

    if-eqz v2, :cond_0

    const-string v3, "writeToParcel.(Landroid/os/Parcel;I)V"

    const/4 v4, 0x3

    new-array v4, v4, [Ljava/lang/Object;

    aput-object p0, v4, v1

    aput-object p1, v4, v0

    const/4 v0, 0x2

    new-instance v1, Ljava/lang/Integer;

    invoke-direct {v1, p2}, Ljava/lang/Integer;-><init>(I)V

    aput-object v1, v4, v0

    invoke-interface {v2, v3, v4}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    .line 77
    :goto_0
    return-void

    .line 70
    :cond_0
    const/16 v2, 0xa49

    invoke-virtual {p1, v2}, Landroid/os/Parcel;->writeInt(I)V

    .line 71
    iget-boolean v2, p0, Lcom/dianping/model/H5FavorConfig;->isPresent:Z

    if-eqz v2, :cond_1

    :goto_1
    invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V

    .line 72
    const/16 v0, 0x293a

    invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V

    .line 73
    iget-object v0, p0, Lcom/dianping/model/H5FavorConfig;->b:[Ljava/lang/String;

    invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeStringArray([Ljava/lang/String;)V

    .line 74
    const v0, 0xd258

    invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V

    .line 75
    iget-object v0, p0, Lcom/dianping/model/H5FavorConfig;->a:[Ljava/lang/String;

    invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeStringArray([Ljava/lang/String;)V

    .line 76
    const/4 v0, -0x1

    invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V

    goto :goto_0

    :cond_1
    move v0, v1

    .line 71
    goto :goto_1
.end method
"""
# text = '''.class public Lcom/dianping/model/SimpleMsg;
# .super Ljava/lang/Object;
# .source "SimpleMsg.java"
#
# # interfaces
# .implements Landroid/os/Parcelable;
# .implements Lcom/dianping/archive/b;
#
#
# # static fields
# .field public static volatile synthetic $change:Lcom/dianping/android/hotfix/IncrementalChange;
#
# .field public static final CREATOR:Landroid/os/Parcelable$Creator;
#     .annotation system Ldalvik/annotation/Signature;
#         value = {
#             "Landroid/os/Parcelable$Creator",
#             "<",
#             "Lcom/dianping/model/SimpleMsg;",
#             ">;"
#         }
#     .end annotation
# .end field
#
# .field public static final a:Lcom/dianping/archive/c;
#     .annotation system Ldalvik/annotation/Signature;
#         value = {
#             "Lcom/dianping/archive/c",
#             "<",
#             "Lcom/dianping/model/SimpleMsg;",
#             ">;"
#         }
#     .end annotation
# .end field
#
#
# # instance fields
# .field public b:Z
#
# .field public c:Ljava/lang/String;
#
# .field public d:I
#
# .field public e:I
#
# .field public f:Ljava/lang/String;
#
# .field public g:Ljava/lang/String;
#
# .field public h:I
#
# .field public i:I
#
# .field public j:I
#
# .field public k:Ljava/lang/String;
#
#
# # direct methods
# .method public static constructor <clinit>()V
#     .locals 1
#
#     .prologue
#     .line 21
#     new-instance v0, Lcom/dianping/model/SimpleMsg$1;
#
#     invoke-direct {v0}, Lcom/dianping/model/SimpleMsg$1;-><init>()V
#
#     sput-object v0, Lcom/dianping/model/SimpleMsg;->a:Lcom/dianping/archive/c;
#
#     .line 37
#     new-instance v0, Lcom/dianping/model/SimpleMsg$2;
#
#     invoke-direct {v0}, Lcom/dianping/model/SimpleMsg$2;-><init>()V
#
#     sput-object v0, Lcom/dianping/model/SimpleMsg;->CREATOR:Landroid/os/Parcelable$Creator;
#
#     return-void
# .end method
#
# .method public constructor <init>()V
#     .locals 2
#
#     .prologue
#     const/4 v1, 0x0
#
#     .line 99
#     invoke-direct {p0}, Ljava/lang/Object;-><init>()V
#
#     .line 100
#     const/4 v0, 0x1
#
#     iput-boolean v0, p0, Lcom/dianping/model/SimpleMsg;->b:Z
#
#     .line 101
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->j:I
#
#     .line 102
#     const-string v0, ""
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     .line 103
#     const-string v0, ""
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     .line 104
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->h:I
#
#     .line 105
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->i:I
#
#     .line 106
#     const-string v0, ""
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->k:Ljava/lang/String;
#
#     .line 107
#     const-string v0, ""
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->c:Ljava/lang/String;
#
#     .line 108
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->d:I
#
#     .line 109
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->e:I
#
#     .line 110
#     return-void
# .end method
#
# .method public constructor <init>(Landroid/os/Parcel;)V
#     .locals 2
#
#     .prologue
#     const/4 v0, 0x1
#
#     .line 125
#     invoke-direct {p0}, Ljava/lang/Object;-><init>()V
#
#     .line 126
#     invoke-virtual {p1}, Landroid/os/Parcel;->readInt()I
#
#     move-result v1
#
#     if-ne v1, v0, :cond_0
#
#     :goto_0
#     iput-boolean v0, p0, Lcom/dianping/model/SimpleMsg;->b:Z
#
#     .line 127
#     invoke-virtual {p1}, Landroid/os/Parcel;->readInt()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->j:I
#
#     .line 128
#     invoke-virtual {p1}, Landroid/os/Parcel;->readString()Ljava/lang/String;
#
#     move-result-object v0
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     .line 129
#     invoke-virtual {p1}, Landroid/os/Parcel;->readString()Ljava/lang/String;
#
#     move-result-object v0
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     .line 130
#     invoke-virtual {p1}, Landroid/os/Parcel;->readInt()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->h:I
#
#     .line 131
#     invoke-virtual {p1}, Landroid/os/Parcel;->readInt()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->i:I
#
#     .line 132
#     invoke-virtual {p1}, Landroid/os/Parcel;->readString()Ljava/lang/String;
#
#     move-result-object v0
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->k:Ljava/lang/String;
#
#     .line 133
#     invoke-virtual {p1}, Landroid/os/Parcel;->readString()Ljava/lang/String;
#
#     move-result-object v0
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->c:Ljava/lang/String;
#
#     .line 134
#     invoke-virtual {p1}, Landroid/os/Parcel;->readInt()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->d:I
#
#     .line 135
#     invoke-virtual {p1}, Landroid/os/Parcel;->readInt()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->e:I
#
#     .line 136
#     return-void
#
#     .line 126
#     :cond_0
#     const/4 v0, 0x0
#
#     goto :goto_0
# .end method
#
# .method public constructor <init>(Ljava/lang/String;Ljava/lang/String;I)V
#     .locals 1
#
#     .prologue
#     .line 59
#     invoke-direct {p0}, Ljava/lang/Object;-><init>()V
#
#     .line 60
#     const/4 v0, 0x1
#
#     iput-boolean v0, p0, Lcom/dianping/model/SimpleMsg;->b:Z
#
#     .line 61
#     iput-object p1, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     .line 62
#     iput-object p2, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     .line 63
#     iput p3, p0, Lcom/dianping/model/SimpleMsg;->j:I
#
#     .line 64
#     return-void
# .end method
#
# .method public constructor <init>(Ljava/lang/String;Ljava/lang/String;II)V
#     .locals 1
#
#     .prologue
#     .line 67
#     invoke-direct {p0}, Ljava/lang/Object;-><init>()V
#
#     .line 68
#     const/4 v0, 0x1
#
#     iput-boolean v0, p0, Lcom/dianping/model/SimpleMsg;->b:Z
#
#     .line 69
#     iput-object p1, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     .line 70
#     iput-object p2, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     .line 71
#     iput p3, p0, Lcom/dianping/model/SimpleMsg;->h:I
#
#     .line 72
#     iput p4, p0, Lcom/dianping/model/SimpleMsg;->i:I
#
#     .line 73
#     return-void
# .end method
#
# .method public constructor <init>(Z)V
#     .locals 2
#
#     .prologue
#     const/4 v1, 0x0
#
#     .line 112
#     invoke-direct {p0}, Ljava/lang/Object;-><init>()V
#
#     .line 113
#     iput-boolean p1, p0, Lcom/dianping/model/SimpleMsg;->b:Z
#
#     .line 114
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->j:I
#
#     .line 115
#     const-string v0, ""
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     .line 116
#     const-string v0, ""
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     .line 117
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->h:I
#
#     .line 118
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->i:I
#
#     .line 119
#     const-string v0, ""
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->k:Ljava/lang/String;
#
#     .line 120
#     const-string v0, ""
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->c:Ljava/lang/String;
#
#     .line 121
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->d:I
#
#     .line 122
#     iput v1, p0, Lcom/dianping/model/SimpleMsg;->e:I
#
#     .line 123
#     return-void
# .end method
#
#
# # virtual methods
# .method public a()I
#     .locals 4
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_0
#
#     const-string v1, "a.()I"
#
#     const/4 v2, 0x1
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Ljava/lang/Number;
#
#     invoke-virtual {v0}, Ljava/lang/Number;->intValue()I
#
#     move-result v0
#
#     .line 139
#     :goto_0
#     return v0
#
#     :cond_0
#     iget v0, p0, Lcom/dianping/model/SimpleMsg;->j:I
#
#     goto :goto_0
# .end method
#
# .method public b()Ljava/lang/String;
#     .locals 4
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_0
#
#     const-string v1, "b.()Ljava/lang/String;"
#
#     const/4 v2, 0x1
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Ljava/lang/String;
#
#     .line 143
#     :goto_0
#     return-object v0
#
#     :cond_0
#     iget-object v0, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     goto :goto_0
# .end method
#
# .method public c()Ljava/lang/String;
#     .locals 4
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_0
#
#     const-string v1, "c.()Ljava/lang/String;"
#
#     const/4 v2, 0x1
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Ljava/lang/String;
#
#     .line 147
#     :goto_0
#     return-object v0
#
#     :cond_0
#     iget-object v0, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     goto :goto_0
# .end method
#
# .method public d()I
#     .locals 4
#     .annotation runtime Ljava/lang/Deprecated;
#     .end annotation
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_0
#
#     const-string v1, "d.()I"
#
#     const/4 v2, 0x1
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Ljava/lang/Number;
#
#     invoke-virtual {v0}, Ljava/lang/Number;->intValue()I
#
#     move-result v0
#
#     .line 156
#     :goto_0
#     return v0
#
#     :cond_0
#     iget v0, p0, Lcom/dianping/model/SimpleMsg;->h:I
#
#     goto :goto_0
# .end method
#
# .method public decode(Lcom/dianping/archive/d;)V
#     .locals 4
#     .annotation system Ldalvik/annotation/Throws;
#         value = {
#             Lcom/dianping/archive/a;
#         }
#     .end annotation
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_1
#
#     const-string v1, "decode.(Lcom/dianping/archive/d;)V"
#
#     const/4 v2, 0x2
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     const/4 v3, 0x1
#
#     aput-object p1, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     .line 216
#     :cond_0
#     return-void
#
#     .line 182
#     :sswitch_0
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->b()Z
#
#     move-result v0
#
#     iput-boolean v0, p0, Lcom/dianping/model/SimpleMsg;->b:Z
#
#     .line 179
#     :cond_1
#     :goto_0
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->j()I
#
#     move-result v0
#
#     if-lez v0, :cond_0
#
#     .line 180
#     sparse-switch v0, :sswitch_data_0
#
#     .line 212
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->i()V
#
#     goto :goto_0
#
#     .line 185
#     :sswitch_1
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->c()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->j:I
#
#     goto :goto_0
#
#     .line 188
#     :sswitch_2
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->g()Ljava/lang/String;
#
#     move-result-object v0
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     goto :goto_0
#
#     .line 191
#     :sswitch_3
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->g()Ljava/lang/String;
#
#     move-result-object v0
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     goto :goto_0
#
#     .line 194
#     :sswitch_4
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->c()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->h:I
#
#     goto :goto_0
#
#     .line 197
#     :sswitch_5
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->c()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->i:I
#
#     goto :goto_0
#
#     .line 200
#     :sswitch_6
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->g()Ljava/lang/String;
#
#     move-result-object v0
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->k:Ljava/lang/String;
#
#     goto :goto_0
#
#     .line 203
#     :sswitch_7
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->g()Ljava/lang/String;
#
#     move-result-object v0
#
#     iput-object v0, p0, Lcom/dianping/model/SimpleMsg;->c:Ljava/lang/String;
#
#     goto :goto_0
#
#     .line 206
#     :sswitch_8
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->c()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->d:I
#
#     goto :goto_0
#
#     .line 209
#     :sswitch_9
#     invoke-virtual {p1}, Lcom/dianping/archive/d;->c()I
#
#     move-result v0
#
#     iput v0, p0, Lcom/dianping/model/SimpleMsg;->e:I
#
#     goto :goto_0
#
#     .line 180
#     nop
#
#     :sswitch_data_0
#     .sparse-switch
#         0x8d -> :sswitch_1
#         0xa49 -> :sswitch_0
#         0x36e9 -> :sswitch_2
#         0x44fb -> :sswitch_8
#         0x57b6 -> :sswitch_3
#         0x63ea -> :sswitch_6
#         0x7368 -> :sswitch_7
#         0x73ad -> :sswitch_5
#         0xb0bb -> :sswitch_4
#         0xefe5 -> :sswitch_9
#     .end sparse-switch
# .end method
#
# .method public describeContents()I
#     .locals 4
#
#     .prologue
#     const/4 v0, 0x0
#
#     .line 0
#     sget-object v1, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v1, :cond_0
#
#     const-string v2, "describeContents.()I"
#
#     const/4 v3, 0x1
#
#     new-array v3, v3, [Ljava/lang/Object;
#
#     aput-object p0, v3, v0
#
#     invoke-interface {v1, v2, v3}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Ljava/lang/Number;
#
#     invoke-virtual {v0}, Ljava/lang/Number;->intValue()I
#
#     move-result v0
#
#     .line 260
#     :cond_0
#     return v0
# .end method
#
# .method public e()I
#     .locals 4
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_0
#
#     const-string v1, "e.()I"
#
#     const/4 v2, 0x1
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Ljava/lang/Number;
#
#     invoke-virtual {v0}, Ljava/lang/Number;->intValue()I
#
#     move-result v0
#
#     .line 160
#     :goto_0
#     return v0
#
#     :cond_0
#     iget v0, p0, Lcom/dianping/model/SimpleMsg;->i:I
#
#     goto :goto_0
# .end method
#
# .method public f()Ljava/lang/String;
#     .locals 4
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_0
#
#     const-string v1, "f.()Ljava/lang/String;"
#
#     const/4 v2, 0x1
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Ljava/lang/String;
#
#     .line 164
#     :goto_0
#     return-object v0
#
#     :cond_0
#     iget-object v0, p0, Lcom/dianping/model/SimpleMsg;->k:Ljava/lang/String;
#
#     goto :goto_0
# .end method
#
# .method public g()Lcom/dianping/archive/DPObject;
#     .locals 4
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_0
#
#     const-string v1, "g.()Lcom/dianping/archive/DPObject;"
#
#     const/4 v2, 0x1
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Lcom/dianping/archive/DPObject;
#
#     .line 264
#     :goto_0
#     return-object v0
#
#     :cond_0
#     new-instance v0, Lcom/dianping/archive/DPObject;
#
#     const-string v1, "SimpleMsg"
#
#     invoke-direct {v0, v1}, Lcom/dianping/archive/DPObject;-><init>(Ljava/lang/String;)V
#
#     invoke-virtual {v0}, Lcom/dianping/archive/DPObject;->b()Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "IsPresent"
#
#     iget-boolean v2, p0, Lcom/dianping/model/SimpleMsg;->b:Z
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;Z)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "StatusCode"
#
#     iget v2, p0, Lcom/dianping/model/SimpleMsg;->j:I
#
#     .line 265
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;I)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "Title"
#
#     iget-object v2, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;Ljava/lang/String;)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "Content"
#
#     iget-object v2, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;Ljava/lang/String;)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "Icon"
#
#     iget v2, p0, Lcom/dianping/model/SimpleMsg;->h:I
#
#     .line 266
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;I)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "Flag"
#
#     iget v2, p0, Lcom/dianping/model/SimpleMsg;->i:I
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;I)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "Data"
#
#     iget-object v2, p0, Lcom/dianping/model/SimpleMsg;->k:Ljava/lang/String;
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;Ljava/lang/String;)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "ErrorMsg"
#
#     iget-object v2, p0, Lcom/dianping/model/SimpleMsg;->c:Ljava/lang/String;
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;Ljava/lang/String;)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "ErrorCode"
#
#     iget v2, p0, Lcom/dianping/model/SimpleMsg;->d:I
#
#     .line 267
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;I)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     const-string v1, "ReturnID"
#
#     iget v2, p0, Lcom/dianping/model/SimpleMsg;->e:I
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/archive/DPObject$e;->b(Ljava/lang/String;I)Lcom/dianping/archive/DPObject$e;
#
#     move-result-object v0
#
#     invoke-interface {v0}, Lcom/dianping/archive/DPObject$e;->a()Lcom/dianping/archive/DPObject;
#
#     move-result-object v0
#
#     goto :goto_0
# .end method
#
# .method public toString()Ljava/lang/String;
#     .locals 4
#
#     .prologue
#     .line 0
#     sget-object v0, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v0, :cond_0
#
#     const-string v1, "toString.()Ljava/lang/String;"
#
#     const/4 v2, 0x1
#
#     new-array v2, v2, [Ljava/lang/Object;
#
#     const/4 v3, 0x0
#
#     aput-object p0, v2, v3
#
#     invoke-interface {v0, v1, v2}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     move-result-object v0
#
#     check-cast v0, Ljava/lang/String;
#
#     .line 173
#     :goto_0
#     return-object v0
#
#     :cond_0
#     new-instance v0, Ljava/lang/StringBuilder;
#
#     invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
#
#     iget-object v1, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
#
#     move-result-object v0
#
#     const-string v1, " : "
#
#     invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
#
#     move-result-object v0
#
#     iget-object v1, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
#
#     move-result-object v0
#
#     invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
#
#     move-result-object v0
#
#     goto :goto_0
# .end method
#
# .method public writeToParcel(Landroid/os/Parcel;I)V
#     .locals 5
#
#     .prologue
#     const/4 v0, 0x1
#
#     const/4 v1, 0x0
#
#     .line 0
#     sget-object v2, Lcom/dianping/model/SimpleMsg;->$change:Lcom/dianping/android/hotfix/IncrementalChange;
#
#     if-eqz v2, :cond_0
#
#     const-string v3, "writeToParcel.(Landroid/os/Parcel;I)V"
#
#     const/4 v4, 0x3
#
#     new-array v4, v4, [Ljava/lang/Object;
#
#     aput-object p0, v4, v1
#
#     aput-object p1, v4, v0
#
#     const/4 v0, 0x2
#
#     new-instance v1, Ljava/lang/Integer;
#
#     invoke-direct {v1, p2}, Ljava/lang/Integer;-><init>(I)V
#
#     aput-object v1, v4, v0
#
#     invoke-interface {v2, v3, v4}, Lcom/dianping/android/hotfix/IncrementalChange;->access$dispatch(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;
#
#     .line 256
#     :goto_0
#     return-void
#
#     .line 246
#     :cond_0
#     iget-boolean v2, p0, Lcom/dianping/model/SimpleMsg;->b:Z
#
#     if-eqz v2, :cond_1
#
#     :goto_1
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V
#
#     .line 247
#     iget v0, p0, Lcom/dianping/model/SimpleMsg;->j:I
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V
#
#     .line 248
#     iget-object v0, p0, Lcom/dianping/model/SimpleMsg;->f:Ljava/lang/String;
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V
#
#     .line 249
#     iget-object v0, p0, Lcom/dianping/model/SimpleMsg;->g:Ljava/lang/String;
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V
#
#     .line 250
#     iget v0, p0, Lcom/dianping/model/SimpleMsg;->h:I
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V
#
#     .line 251
#     iget v0, p0, Lcom/dianping/model/SimpleMsg;->i:I
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V
#
#     .line 252
#     iget-object v0, p0, Lcom/dianping/model/SimpleMsg;->k:Ljava/lang/String;
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V
#
#     .line 253
#     iget-object v0, p0, Lcom/dianping/model/SimpleMsg;->c:Ljava/lang/String;
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V
#
#     .line 254
#     iget v0, p0, Lcom/dianping/model/SimpleMsg;->d:I
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V
#
#     .line 255
#     iget v0, p0, Lcom/dianping/model/SimpleMsg;->e:I
#
#     invoke-virtual {p1, v0}, Landroid/os/Parcel;->writeInt(I)V
#
#     goto :goto_0
#
#     :cond_1
#     move v0, v1
#
#     .line 246
#     goto :goto_1
# .end method
# '''
def gen_field(text):
    field_result = ""
    field_template = "'{key}':'{value}',"
    fields = re.search("# instance fields.*?#", text, re.S).group(0)
    fields = re.findall('\.field public (\w+):.*?a = \"(\w+)\".*?.end field', fields, re.S)
    for k, v in fields:
        field_result += field_template.format(key=k, value=v) + '\n'
    print("{\n" + field_result + "}")


def gen_switch(text):
    body = re.search(":sswitch_data_0\n\s+\.sparse-switch(.*?).end sparse-switch", text, re.S).group(1).split('\n')
    raw = []
    for i in body:
        i = i.strip()
        if not i:
            continue
        _ = i.split("->")
        index = _[1].split("_")[1]
        raw.append({"index": index, "hex": _[0].strip(), "tar": _[1].strip()})
    raw = sorted(raw, key=lambda _: int(_['index'], 16))
    return raw


def gen_func(text):
    template = '''
    def j_flag_{}(self):
        """
        {} -> {}
        :return:
        """
        self.result[self.field_map.get('{}', '{}')]=self.archive_d_{}()

    '''
    result = ""
    raw = gen_switch(text)
    text = re.search("method public decode\(Lcom/dianping/archive/d;\)V(.*?):sswitch_data_0\n\s+\.sparse-switch", text, re.S).group(1)
    for case in raw:
        kuai = re.search("{}\n(.*?)goto".format(case['tar']), text, re.S).group(1).split('\n')
        for i in kuai:
            if i.strip().startswith("invoke-virtual"):
                value = re.search("invoke-virtual(.*?)Lcom/dianping/archive/d;->(\w)\((.*?)$", i, re.S)
                value = value.group(2) if not i.endswith("Ljava/lang/Object;") else value.group(2) + "_archive_c"
            elif i.strip().startswith("iput"):
                key = re.search("iput(.*?);->(\w+):", i, re.S).group(2)
        result += template.format(eval(case['hex']), case['hex'], case['tar'], key, key, value)
    print(result)

# gen_func(text)
# gen_field(text)
