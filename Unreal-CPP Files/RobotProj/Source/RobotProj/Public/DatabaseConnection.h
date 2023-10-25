// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "mongocxx/client.hpp"
#include "mongocxx/instance.hpp"
#include "MongoInstance.h"
#include "Tools/UEdMode.h"
#include "DatabaseConnection.generated.h"

UCLASS()
class ROBOTPROJ_API ADatabaseConnection : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ADatabaseConnection();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;
	std::optional<bsoncxx::document::value> getXCoord(std::string robotName);
	mongocxx::collection getCollection();
	bool getDocumentStatus();
	mongocxx::collection robotDocument;
	bool createdDocument;
};
